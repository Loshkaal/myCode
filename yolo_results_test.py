import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Путь к обученной модели
model_path = "D:/Source/myCode/models/yolo_128x128.h5"

# Загрузка обученной модели
model = tf.keras.models.load_model(model_path)
print("Модель загружена успешно.")

# Список классов (замените на ваши метки)
class_labels = ['domik', 'ekomilk', 'ekoniva', 'krepysh', 'nyanya', 'spar']

# Путь к тестовым изображениям
image_folder = "D:/Source/myCode/dataset/test"

# Константы для сообщений
PREPROCESS_MSG = "[ПРЕДОБРАБОТКА]"
CHECK_MSG = "[ПРОВЕРКА]"

def resize_image(image_path, target_size=(128, 128)):
    """Изменение размера и конвертация в RGB"""
    image = cv2.imread(image_path)
    if image is None:
        print(f"{PREPROCESS_MSG} Ошибка: Изображение {os.path.basename(image_path)} не найдено или повреждено.")
        return None

    # Конвертируем BGR -> RGB и ресайз
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    resized_image = cv2.resize(image, target_size)
    print(f"{PREPROCESS_MSG} Изображение {os.path.basename(image_path)} изменено до {target_size}.")
    return resized_image

def check_image(image, expected_size=(128, 128)):
    """Проверка размера и формата"""
    if image is None:
        return False

    if image.shape[:2] != expected_size:
        print(f"{CHECK_MSG} Ошибка: Размер {image.shape[:2]} вместо {expected_size}.")
        return False

    if len(image.shape) != 3 or image.shape[2] != 3:
        print(f"{CHECK_MSG} Ошибка: Неверный формат каналов.")
        return False

    print(f"{CHECK_MSG} Изображение валидно.")
    return True

def predict_image(image):
    """Предсказание для одного изображения"""
    image = image / 255.0  # Нормализация как при обучении
    image = np.expand_dims(image, axis=0)  # Исправлено: expand_dims
    predictions = model.predict(image, verbose=0)
    return class_labels[np.argmax(predictions)]  # Исправлено: индексация

# Получение списка изображений (исправлено расширение -png)
image_files = [
    os.path.join(image_folder, f)
    for f in os.listdir(image_folder)
    if f.lower().endswith(('.jpg', '.png', '.jpeg'))
]

# Этап 1: Ресайз изображений
print("\n--- ЭТАП 1: РЕСАЙЗ ИЗОБРАЖЕНИЙ ---")
resized_images = []
image_names = []

for image_path in image_files:
    resized = resize_image(image_path)
    if resized is not None:
        resized_images.append(resized)
        image_names.append(os.path.basename(image_path))

# Этап 2: Проверка изображений
print("\n--- ЭТАП 2: ПРОВЕРКА ИЗОБРАЖЕНИЙ ---")
valid_images = []
valid_names = []

for img, name in zip(resized_images, image_names):
    if check_image(img):
        valid_images.append(img)
        valid_names.append(name)

# Этап 3: Предсказание классов
print("\n--- ЭТАП 3: ПРЕДСКАЗАНИЕ КЛАССОВ ---")
results = PrettyTable()
results.field_names = ["Изображение", "Предсказание", "Доверие"]

for img, name in zip(valid_images, valid_names):
    # Нормализация и предсказание
    img_normalized = img / 255.0
    pred = model.predict(np.expand_dims(img_normalized, axis=0), verbose=0)

    # Получение метки и уверенности
    class_idx = np.argmax(pred)
    confidence = round(pred[0][class_idx] * 100, 2)

    results.add_row([
        name,
        class_labels[class_idx],
        f"{confidence}%"
    ])

print("\n--- РЕЗУЛЬТАТЫ ---")
print(results)