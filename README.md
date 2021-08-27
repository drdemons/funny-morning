## Funny Morning.
Небольшая программа, написанная исключительно для лулзов.
Умеет здороваться по утрам будних дней и присылает анекдот в выбранный телеграм чат и\или slack канал.

## Прежде чем
* Для Telegram:

Прежде чем воспользоваться, нужно получить api_ip и api_hash для кастомного клиента телеграмма, это можно сделать [тут](https://my.telegram.org/auth?to=apps).
* Для Slack:
 [Create a Slack app](https://github.com/slackapi/python-slack-sdk/blob/main/tutorial/01-creating-the-slack-app.md)

Получить список чатов можно так.
```python
from telethon.sync import TelegramClient

api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'
client = TelegramClient('client', api_id, api_hash)
client.start()

for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)
```
После запуска telethon попросит ввести номер телефона, на него придет код его нужно будет ввести,
после этого сгенериться файл client.session, после этого будет работать без ввода до смены имени сессии.

Так же нужно настроить конфиг это yaml файл со следующим форматом:
```yaml
clients: // можно указывать один клиент или два в зависимости от того куда нужно слать сообщения.
  telegram:
    api_id: // берется на сайте телеграмма по ссылке выше.
    api_hash: // берется там же.
    group_id: // id чата в который будем слать анекдоты.
  slack:
    token: // берется на сайте slack после создания приложения.
    channel: // имя канала в который нужно отравлять сообщения.
scheduler:
  time: '05:00' // Время когда запускается отправка сообщения (время gmt).
  sleep: 20 // Период срабатывания шедулера каждые 20 секунд.
message:
  text: 'Hello all!' // Текст сообщения. 
```

## Quick start.

* Нужно с клонировать репозиторий с github,
  > git clone https://github.com/drdemons/funny-morning.git
* Установить переменную окружения PROFILE.
  > export PROFILE=dev (что бы приложение читало локальный конфиг)
* Выполнить команду:
  > pip install -r requirements.txt
* Запустить файл main.py.
  > python3 main.py

## Start using Docker.
### Локально

1. Конфиг прячется в docker secret, поэтому сначала нужно активировать docker swarm mode если он еще не активирован.
> docker swarm init

2. Затем добавить config в secret.
> docker secret create config config.yaml
###### Важно секрет должен называться config.
###### Файл session должен лежать в директории в которой выполняется эта команда или в docker-compose.yml нужно указать полный путь к этому файлу.

3. Собрать image.
> docker build -t funny-morning .

4. Запустить.
> docker stack deploy --compose-file docker-compose.yml funny-morning

### Загрузка с Docker Hub.

* Получить образ с Docker Hub.
> docker pull 171287/funny-morning

* Выполнить пункт 1, 2, затем 4 из предыдущего руководства =)