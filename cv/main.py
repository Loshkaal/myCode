import pandas as pd
import numpy as np

# Функция для загрузки данных из файла
def load_data(file_path):
    """ Загрузка данных из файла CSV """
    data = pd.read_csv(file_path, delimiter=';')  # Указываем разделитель, если он отличается
    print("Доступные колонки:", data.columns)  # Проверка наименований колонок
    return data

# Функция для расчёта индивидуального индекса загрязнения (ИЗА)
def calculate_IZA(data, pollutant, mpc, a):
    """ Расчет индекса загрязнения для одного загрязнителя """
    # Проверяем наличие колонки загрязнителя
    if pollutant in data.columns:
        data[f'I_{pollutant}'] = (data[pollutant] / mpc) ** a
    else:
        print(f"Колонка {pollutant} не найдена в данных.")
    return data

# Функция для расчёта комплексного индекса загрязнения (КИЗА)
def calculate_KIZA(data, pollutants):
    """ Расчет комплексного индекса загрязнения """
    data['KIZA'] = data[[f'I_{poll}' for poll in pollutants if f'I_{poll}' in data.columns]].sum(axis=1)
    return data['KIZA']

# Функция для оценки уровня загрязнения
def evaluate_pollution_level(KIZA_value):
    """ Определение уровня загрязнения по значению КИЗА """
    if KIZA_value > 10:
        return 'Очень высокое'
    elif KIZA_value > 5:
        return 'Высокое'
    elif KIZA_value > 2:
        return 'Повышенное'
    else:
        return 'Низкое'

# Главная функция программы
def main():
    file_path = 'pollution_data.csv'  # Укажите путь к вашему файлу данных
    data = load_data(file_path)
    
    pollutants = ['SO2', 'NO2', 'CO', 'NH3', 'Phenol']  # Список загрязнителей
    mpcs = [0.05, 0.04, 0.1, 0.02, 0.006]  # Предельно допустимые концентрации (ПДК)
    a_values = [1, 1.3, 0.85, 1.5, 1.5]  # Коэффициенты a для разных классов опасности
    
    for pollutant, mpc, a in zip(pollutants, mpcs, a_values):
        calculate_IZA(data, pollutant, mpc, a)
    
    calculate_KIZA(data, pollutants)
    
    data['Pollution_Level'] = data['KIZA'].apply(evaluate_pollution_level)
    
    data.to_csv('pollution_evaluation_results.csv', index=False)  # Сохраняем результаты
    print("Результаты оценки загрязнения сохранены в файл 'pollution_evaluation_results.csv'")

if __name__ == '__main__':
    main()

#pollution_data.csv