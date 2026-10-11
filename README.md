Скрипт скачивает один и тот же файл 10 раз подряд и показывает среднее время запроса, объем скачанных данных и скорость в MB/s

По умолчанию качается панорама Млечного Пути от ESO весом около 8 MB

Установка

```
git clone https://github.com/AlexAsadullin/network-speed-measure.git
cd network-speed-measure
uv venv
```

Запуск с адресом по умолчанию

```
uv run speedtest.py
```

Запуск со своим адресом

```
uv run speedtest.py https://esahubble.org/media/archives/images/large/heic0506a.jpg
```

Запуск без uv

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

Зависимостей нет, нужен только Python 3.12 или новее, uv по желанию
