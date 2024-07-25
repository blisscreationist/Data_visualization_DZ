import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.divan.ru/category/pramye-divany'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим элементы с ценами
    price_elements = soup.find_all('span', {'data-testid': 'price'})

    # Создаем CSV-файл
    with open('prices.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Price'])

        for price_element in price_elements:
            price_text = price_element.get_text(strip=True)
            price_text = price_text.replace('руб.', '').replace(' ', '')  # Удаляем 'руб.' и пробелы
            csvwriter.writerow([price_text])
else:
    print(f'Ошибка при запросе страницы: {response.status_code}')

# Чтение данных CSV-файла
df = pd.read_csv('prices.csv')

# Преобразуем колонку 'Price' в числовой формат
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Вычисляем среднюю цену
average_price = df['Price'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} руб.')

# Строим гистограмму цен на диваны
plt.figure(figsize=(10, 6))
plt.hist(df['Price'].dropna(), bins=20, edgecolor='black')
plt.title('Распределение цен на диваны')
plt.xlabel('Цена (руб.)')
plt.ylabel('Количество')
plt.grid(True)
plt.show()