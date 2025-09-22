# HTTP-клиент для работы с запросами
import requests

# Эндпоинт калькулятора Banki.ru; DNS-резолвинг и TLS выполняются стеком ОС/requests
url = "https://www.banki.ru/products/hypothec/api/v1/calculator/"

# Параметры GET-запроса (формируются в query-строку ?key=value&…)
params = {
    "initial_fee": 2500000,  # было 'inital_fee' — опечатка
    "period": 7665,
    "rate": 10.5,
    "realty_price": 4000000,
    "type": "by-cost",
    "monthlyPay": 14162.73,
}

# Заголовки: запрашиваем JSON и имитируем браузерный клиент при необходимости
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.5",
    "Referer": "https://www.banki.ru/products/hypothec/domrfbank/calculator/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
    "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Brave";v="140"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-full-version-list": '"Chromium";v="140.0.0.0", "Not=A?Brand";v="24.0.0.0", "Brave";v="140.0.0.0"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"19.0.0"',
}

# Выполняем GET с query-параметрами; requests сам соберёт URL и отправит запрос
response = requests.get(url=url, headers=headers, params=params, timeout=15)

# Декодируем тело ответа как JSON в структуры Python (dict/list)
response_dict = response.json()

print(response_dict)
