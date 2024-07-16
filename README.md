## Для запуска проекта необходимо
- Установить зависимости из requirements.txt
- Развернуть S3 Сервер.
  - Создать ключ доступа к S3 серверу.
  - В файле extensions.py:
    - Указать ключ доступа в поле cred.
    - Указать имя S3 ведра в поле BUCKET.
    - Указать адрес S3 сервера в поле api_url.
  - #ЗАМЕТКА : в будущем ключи будут перенесены в конфиг файл / переменные окружения
- Запустить FastAPI используя команду "fastapi dev main.py"


## Тестирование функций
Для тестирования можно воспользоваться Swagger Docs по адресу http://localhost:8000/docs
