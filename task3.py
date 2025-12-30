import requests
import matplotlib.pyplot as plt
from datetime import datetime

url = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20251025&end=20251031&valcode=eur&sort=exchangedate&order=asc&json"
response = requests.get(url)
data = response.json()

# Вилучення дати й курсу для побудови графіка
dates = [item['exchangedate'] for item in data]
rates = [item['rate'] for item in data]

# Перетворення рядків з датами в об'єкти datetime для коректного відображення
dates = [datetime.strptime(d, '%d.%m.%Y') for d in dates]

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(dates, rates, marker='o', linestyle='-', color='b', label='Rate EUR')

# Кастомізація
plt.title('Exchange rate (EUR)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Rate (UAH)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()