import requests

url = "https://catalog.onliner.by/"  # Замените на ваш URL
response = requests.get(url)

# Проверка статуса ответа
print(response.text)