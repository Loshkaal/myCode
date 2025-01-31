import os
from pathlib import Path

def main():
    # 1. Вставьте свой путь сюда ↓
    TARGET_DIR = Path("D:/working/10870/10870")
    
    # 2. Проверка существования папки
    if not TARGET_DIR.exists() or not TARGET_DIR.is_dir():
        print(f"Ошибка: Папка {TARGET_DIR} не найдена!")
        return

    # 3. Получаем и сортируем папки
    folders = sorted([f for f in TARGET_DIR.iterdir() if f.is_dir()])
    
    # 4. Проверка количества
    if len(folders) != 183:
        print(f"Ошибка: Найдено {len(folders)} папок вместо 39!")
        return

    # 5. Переименовываем
    for index, folder in enumerate(folders):
        new_name = str(index)
        new_path = folder.parent / new_name
        
        try:
            folder.rename(new_path)
            print(f"Успешно: {folder.name} -> {new_name}")
        except Exception as e:
            print(f"Ошибка с {folder.name}: {str(e)}")
            break  # Останавливаем при первой ошибке

if __name__ == "__main__":
    main()
    print("Готово! Закройте это окно.")