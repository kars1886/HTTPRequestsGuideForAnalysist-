# Импортируем библиотеку requests для работы с HTTP-запросами
import requests

# URL и заголовки для запроса (адрес определяется уже под капотом с помощью DNS)
# В данном случае мы указываем формат сразу в URL
# Документация для данного эндпоинта https://iss.moex.com/iss/reference/205
url = "https://iss.moex.com/iss/securities.json"

# query параметры запроса
params = {"is_trading": 0}

# Заголовки запроса
headers = {"Accept": "application/json"}

# Выполняем GET-запрос к указанному URL с заданными заголовками и адресом
# response это объект класса Response, который содержит информацию о запросе и ответе сервера
response = requests.get(url=url, headers=headers, params=params)

# Парсим ответ сервера в формате JSON
response_dict = response.json()

print(response_dict)

