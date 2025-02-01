import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os
import torch
from PIL import Image

# Гиперпараметры
IMG_SIZE = 128  # Увеличенный размер для лучшего качества
BATCH_SIZE = 32
EPOCHS = 30

# Создаем папку для моделей, если её нет
if not os.path.exists("D:/Source/myCode/models"):
    os.makedirs("D:/Source/myCode/models")

# Аугментация данных для тренировочного набора
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

# Загрузка тренировочных данных
train_data = train_datagen.flow_from_directory(
    "D:/Source/myCode/dataset",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

# Загрузка валидационных данных (без аугментации)
val_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
val_data = val_datagen.flow_from_directory(
    "D:/Source/myCode/dataset",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# Создание модели
base_model = MobileNetV2(
    input_shape=(IMG_SIZE, IMG_SIZE, 3),
    include_top=False,
    weights='imagenet'
)

base_model.trainable = False  # Замораживаем базовую модель

model = models.Sequential([
    base_model,
    layers.Conv2D(256, (3,3), activation='relu', padding='same'),  # Добавленный слой
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(train_data.num_classes, activation='softmax')
])

# Размораживание части слоев для тонкой настройки
base_model.trainable = True
for layer in base_model.layers[:100]:
    layer.trainable = False

# Компиляция модели
model.compile(
    optimizer=optimizers.Adam(learning_rate=1e-4),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Обучение модели
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=EPOCHS
)

# Оценка точности
train_loss, train_acc = model.evaluate(train_data)
val_loss, val_acc = model.evaluate(val_data)

print(f"\nТочность на обучающих данных: {train_acc * 100:.2f}%")
print(f"Точность на валидационных данных: {val_acc * 100:.2f}%")

# Сохранение модели
model_name = "yolo_128x128.h5"
model_save_path = os.path.join("D:/Source/myCode/models", model_name)
model.save(model_save_path)
print(f"\nМодель сохранена как: {model_save_path}")

# Обнаружение объектов с помощью YOLOv5
def load_data(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            images.append(os.path.join(directory, filename))
    return images

def detect_objects(images):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    results = model(images)
    return results

def save_results(results, output_directory):
    results.save(save_dir=output_directory)

# Загрузка данных для обнаружения объектов
train_images = load_data("D:/Source/myCode/dataset/train")
val_images = load_data("D:/Source/myCode/dataset/val")
output_directory = "D:/Source/myCode/models"

# Обнаружение объектов и сохранение результатов
train_results = detect_objects(train_images)
val_results = detect_objects(val_images)

save_results(train_results, output_directory)
save_results(val_results, output_directory)

print("Обнаружение объектов завершено. Результаты сохранены в:", output_directory)