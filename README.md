# MoonPayAutoReg
This is MoonPay AutoReg for the https://www.moonpay.com/web3-passport website, it allows you to waitlist all of the mails from "mails.txt" 

Пока не поддерживает прокси, и вполне возможно что ваши почты улетят в антифрод

Установка:
переносим все файлы в папку, в пути не должно быть кириллицы и пробелов

- win+r -> cmd
- cd /d ПутьКФайлу ex: cd /d C:TwitterMultiActions
- pip install -r requirements.txt
- python main.py


поменяйте chromedriver в папке на свою версию хрома.
Как узнать свою версию хрома?
- Нажимаем на 3 точки справа сверху в хроме
- переходим в Справка -> О Браузере Google Chrome
- Запоминаем нашу версию (первые 3 цифры)
- Переходим на https://chromedriver.chromium.org/downloads и устанавливаем версию, идентичную с версией хрома (для меня это 108)


В mails.txt вписываем почты, на каждую стоку 1 почта
