# Импортируем библиотеку requests для работы с HTTP-запросами
import requests

# URL и заголовки для запроса (адрес определяется уже под капотом с помощью DNS)
# Документация для данного эндпоинта https://docs.bitfinex.com/reference/rest-public-market-average-price
url = "https://api-pub.bitfinex.com/v2/calc/trade/avg"

# Параметры запроса в формате JSON для POST запроса
json_params = {
    "symbol": "tBTCUSD",
    "amount": 0.1,
}

# Заголовки запроса
headers = {"Accept": "application/json"}

# Выполняем POST запрос к указанному URL с заданными заголовками и адресом
# response это объект класса Response, который содержит информацию о запросе и ответе сервера
response = requests.post(url=url, headers=headers, json=json_params)

# Парсим ответ сервера в формате JSON
response_dict = response.json()

print(response_dict)

