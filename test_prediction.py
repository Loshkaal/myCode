import tensorflow as tf
import numpy as np
import cv2
import os
from prettytable import PrettyTable

# Загрузка модели
model_path = "D:/Source/myCode/models/product_recognition_model_v4_128x05.h5"
model = tf.keras.models.load_model(model_path)

# Автоматическое определение class_labels из структуры папок
train_data_path = "D:/Source/myCode/dataset/train"
class_labels = sorted(os.listdir(train_data_path))
print(f"Классы, определенные на основе структуры данных: {class_labels}")

# Путь к тестовым изображениям
image_folder = "D:/Source/myCode/dataset/test"

# Константы для сообщений
PREPROCESS_MSG = "[ПРЕОБРАБОТКА]"
CHECK_MSG = "[ПРОВЕРКА]"

def resize_image(image_path, target_size=(128, 128)):
    """Изменение размера и конвертация в RGB"""
    if not os.path.exists(image_path):
        print(f"{PREPROCESS_MSG} Ошибка: Изображение {os.path.basename(image_path)} не найдено или повреждено.")
        return None
    image = cv2.imread(image_path)
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
    image = np.expand_dims(image, axis=0)
    predictions = model.predict(image, verbose=0)
    class_idx = np.argmax(predictions)
    confidence = round(predictions[0][class_idx] * 100, 2)
    return class_labels[class_idx], confidence

# Получение списка изображений
image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

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
    class_name, confidence = predict_image(img)
    results.add_row([name, class_name, f"{confidence}%"])

print("\n--- РЕЗУЛЬТАТЫ ---")
print(results)