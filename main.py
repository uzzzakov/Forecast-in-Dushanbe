import requests


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


CITY = "Dushanbe, TJ"
APPID = "6380aaa71d6a2a9c4dbcd7d8ce9da275"

# https://api.openweathermap.org/data/2.5/weather?q=Dushanbe,TJ&APPID=6380aaa71d6a2a9c4dbcd7d8ce9da275&lang=ru&units=metric
res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': CITY, 'units': 'metric', 'lang': 'ru', 'APPID': APPID})
data = res.json()

print(bcolors.BOLD + bcolors.OKGREEN + "Прогноз погоды на сегодня: " + bcolors.ENDC)
print("Город:", CITY, "🇹🇯")
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", '{0:+3.0f}'.format(data['main']['temp']) + "°C")
print("Скорость ветра:", data['wind']['speed'], "м/с")
print("Видимость:", data['visibility'], "м")
print(bcolors.WARNING + "____________________________" + bcolors.ENDC)

# https://api.openweathermap.org/data/2.5/forecast?q=Dushanbe,TJ&APPID=6380aaa71d6a2a9c4dbcd7d8ce9da275&lang=ru&units=metric
res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': CITY, 'units': 'metric', 'lang': 'ru', 'APPID': APPID})
data = res.json()
cnt = 0
o = 0
print(bcolors.BOLD + bcolors.FAIL + "Прогноз погоды на неделю:" + bcolors.ENDC)
for i in data['list']:
    o = cnt % 8
    if o == 3:
        print("Дата:", i['dt_txt'],
              "\nТемпература:", '{0:+3.0f}'.format(i['main']['temp']) + "°C",
              "\nПогодные условия:", i['weather'][0]['description'],
              "\nСкорость ветра:", i['wind']['speed'], "м/с",
              "\nВидимость:", i['visibility'], "м")
        print(bcolors.WARNING + "____________________________" + bcolors.ENDC)
    cnt += 1
