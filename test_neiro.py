import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import cv2
import os

# Гиперпараметры
IMG_SIZE = 96  # Размер входного изображения
BATCH_SIZE = 32
EPOCHS = 30

# Загрузка и подготовка данных
data_dir = "D:/Source/myCode/dataset"  # Папка с изображениями товаров

datagen = keras.preprocessing.image.ImageDataGenerator(
    rescale=1.0/255,  # Нормализация
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    data_dir,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)
print("Список классов:", train_data.class_indices)  # Вывод списка классов


val_data = datagen.flow_from_directory(
    data_dir,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# Создание модели на основе MobileNetV2
base_model = keras.applications.MobileNetV2(input_shape=(IMG_SIZE, IMG_SIZE, 3), include_top=False, weights='imagenet')
base_model.trainable = False  # Замораживаем веса предобученной модели

model = keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(train_data.num_classes, activation='softmax')
])

# Компиляция модели
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Обучение модели
model.fit(train_data, validation_data=val_data, epochs=EPOCHS)



train_loss, train_acc = model.evaluate(train_data)
val_loss, val_acc = model.evaluate(val_data)

print(f"Точность на обучающих данных: {train_acc * 100:.2f}%")
print(f"Точность на валидационных данных: {val_acc * 100:.2f}%")


# Сохранение модели
model.save("D:/Source/myCode/models/product_recognition_model_v3_96x96.h5")

sample_images, sample_labels = next(iter(train_data))  # Берем первую партию изображений
predictions = model.predict(sample_images)

# Выводим реальные и предсказанные классы
print("Реальные классы:", np.argmax(sample_labels, axis=1))
print("Предсказанные классы:", np.argmax(predictions, axis=1))




