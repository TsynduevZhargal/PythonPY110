import requests

key = "1fcbf37d-2013-4645-9a0a-2dadc99de042"
lat = "59.93"
lon = "30.31"

url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"
headers={"X-Yandex-API-Key": f"{key}"}

response = requests.get(url, headers=headers)
print(response.json())

# Словарь перевода значений направления ветра
DIRECTION_TRANSFORM = {
    'n': 'северное',
    'nne': 'северо - северо - восточное',
    'ne': 'северо - восточное',
    'ene': 'восточно - северо - восточное',
    'e': 'восточное',
    'ese': 'восточно - юго - восточное',
    'se': 'юго - восточное',
    'sse': 'юго - юго - восточное',
    's': 'южное',
    'ssw': 'юго - юго - западное',
    'sw': 'юго - западное',
    'wsw': 'западно - юго - западное',
    'w': 'западное',
    'wnw': 'западно - северо - западное',
    'nw': 'северо - западное',
    'nnw': 'северо - северо - западное',
    'c': 'штиль',
}


def current_weather(lat, lon):
    """
    Описание функции, входных и выходных переменных
    """
    token = '1fcbf37d-2013-4645-9a0a-2dadc99de042'  # Вставить ваш токен
    url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"
    headers = {"X-Yandex-API-Key": f"{token}"}
    response = requests.get(url, headers=headers)
    data = response.json()

    result = {
        'city': ['geo_object']['locality']['name'],
        'time': ['fact']['uptime'],
        'temp': ['fact']['temp'],   # TODO Реализовать вычисление температуры из данных полученных от API
        'feels_like_temp': ['fact']['feels_like'],  # TODO Реализовать вычисление ощущаемой температуры из данных полученных от API
        'pressure': ['fact']['pressure_mm'],  # TODO Реализовать вычисление давления из данных полученных от API
        'humidity': ['fact']['humidity'],  # TODO Реализовать вычисление влажности из данных полученных от API
        'wind_speed': ['fact']['wind_speed'],  # TODO Реализовать вычисление скорости ветра из данных полученных от API
        'wind_gust': ['fact']['wind_gust'],  # TODO Реализовать вычисление скорости порывов ветка из данных полученных от API
        'wind_dir': DIRECTION_TRANSFORM.get(data['fact']['wind_dir']),
    }
    return result


if __name__ == "__main__":
    print(current_weather(59.93, 30.31))  # Проверка работы для координат Санкт-Петербурга