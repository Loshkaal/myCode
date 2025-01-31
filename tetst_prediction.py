import tensorflow as tf
import numpy as np
import cv2
import os
from prettytable import PrettyTable

# Загрузка модели
model = tf.keras.models.load_model("D:/Source/myCode/models/product_recognition_model_v3_96x96.h5")

# Задаем список классов
class_labels = ['ekomilk', 'ekoniva', 'domik', 'nyanya', 'spar', 'krepysh']

# Указываем путь к папке с изображениями
image_folder = "D:/Source/myCode/train/"


# Функция для ресайза изображения
def resize_image(image_path, target_size=(96, 96)):
    image = cv2.imread(image_path)
    if image is None:
        print(f"[РЕСАЙЗ] Ошибка: Изображение {os.path.basename(image_path)} не найдено или повреждено.")
        return None
    resized_image = cv2.resize(image, target_size)
    print(f"[РЕСАЙЗ] Изображение {os.path.basename(image_path)} успешно изменено до {target_size}.")
    return resized_image

# Функция для проверки изображений
def check_image(image, expected_size=(96, 96)):
    if image is None:
        return False
    if image.shape[:2] != expected_size:
        print(f"[ПРОВЕРКА] Ошибка: Неверный размер изображения. Ожидалось {expected_size}, получено {image.shape[:2]}.")
        return False
    print(f"[ПРОВЕРКА] Изображение прошло проверку.")
    return True

# Функция для предсказания класса изображения
def predict_image(image):
    image = image / 255.0  # Нормализация
    image = np.expand_dims(image, axis=0)  # Добавление измерения
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions)
    return class_labels[predicted_class]

# Получаем список всех файлов в папке
image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

# Этап 1: Ресайз всех изображений
print("\n--- ЭТАП 1: РЕСАЙЗ ИЗОБРАЖЕНИЙ ---")
resized_images = []
image_names = []

for image_path in image_files:
    resized_image = resize_image(image_path)
    if resized_image is not None:
        resized_images.append(resized_image)
        image_names.append(os.path.basename(image_path))

# Этап 2: Проверка всех изображений
print("\n--- ЭТАП 2: ПРОВЕРКА ИЗОБРАЖЕНИЙ ---")
valid_images = []
valid_names = []

for i, image in enumerate(resized_images):
    if check_image(image):
        valid_images.append(image)
        valid_names.append(image_names[i])

# Этап 3: Предсказание для всех корректных изображений
print("\n--- ЭТАП 3: ПРЕДСКАЗАНИЕ КЛАССОВ ---")
results_table = PrettyTable()
results_table.field_names = ["Имя изображения", "Предсказанный класс"]

for i, image in enumerate(valid_images):
    predicted_class = predict_image(image)
    results_table.add_row([valid_names[i], predicted_class])

# Выводим результаты в виде таблицы
print("\n--- РЕЗУЛЬТАТЫ ПРЕДСКАЗАНИЙ ---")
print(results_table)В