Тестовое задание 
вакансия: https://hh.ru/vacancy/137302319
Асадуллин Александр Дмитриевич
резюме: https://docs.google.com/document/d/1fXxn4w4mvISXwyeMYtSY7k4RiN0tdZKw/edit?usp=drive_link&ouid=111774011381558844983&rtpof=true&sd=true


Скрипт скачивает один и тот же файл 10 раз подряд и показывает среднее время запроса, объем скачанных данных и скорость в MB/s

По умолчанию качается панорама Млечного Пути от ESO весом около 8 MB

Установка

```
git clone https://github.com/AlexAsadullin/network-speed-measure.git
cd network-speed-measure
uv venv
source .venv/bin/activate
uv sync
```

Запуск с адресом по умолчанию

```
uv run speedtest.py
```

Запуск со своим адресом

```
uv run speedtest.py https://esahubble.org/media/archives/images/large/heic0506a.jpg
```

без uv

```
python3 speedtest.py
python3 speedtest.py https://esahubble.org/media/archives/images/large/heic0506a.jpg
```

Пример вывода

```
Target https://cdn.eso.org/images/large/eso0932a.jpg
#1     8.23 MB in   1.28 s
...
#10    8.23 MB in   1.32 s

Average request time 1.29 s
Downloaded 82.29 MB
Speed 6.39 MB/s
```

Требования:
Python 3.12 или новее
uv
