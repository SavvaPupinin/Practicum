При ответе вашего сервера посылайте некоторые основные заголовки:
    1. Date
    2. Content-type
    3. Server
    4. Content-length
    5. Connection: close.
Формат ответа из кода, который включает все заголовки указанные в задании. (connection: close было изменено для 7 задания)

![image](https://user-images.githubusercontent.com/92520538/144825673-6ebf8e73-e24a-4b06-b23d-9e06f07ac025.png)


Создайте файл настроек вашего веб-сервера, в котором можно задать прослушиваемый порт, рабочую директорию, максимальный объем запроса в байтах. Можете добавить собственные настройки по желанию.

![image](https://user-images.githubusercontent.com/92520538/144825712-10dd30bc-87c0-4497-9106-d8809015e5cb.png)

![image](https://user-images.githubusercontent.com/92520538/144825747-aeb7bcfe-40bd-4daf-8b07-eb74e1b48e08.png)

Если файл не найден, сервер передает в сокет специальный код ошибки - 404.

![image](https://user-images.githubusercontent.com/92520538/144825905-274755c1-5b93-4b0a-824d-6a43fcb8adf1.png)

Сервер должен работать в многопоточном режиме.

![image](https://user-images.githubusercontent.com/92520538/144826018-a215b44e-378c-4f51-908d-85d1334261aa.png)

Сервер должен вести логи в следующем формате: Дата запроса. IP-адрес клиента, имя запрошенного файла, код ошибки.

![image](https://user-images.githubusercontent.com/92520538/144826083-d281cf15-0a57-47e3-b305-b17d818160e7.png)


Добавьте возможность запрашивать только определенные типы файлов (.html, .css, .js и так далее). При запросе неразрешенного типа, верните ошибку 403.

![image](https://user-images.githubusercontent.com/92520538/144826132-d79d7d05-b2d6-4e88-b383-187c8d126c3a.png)

Реализуйте поддержку бинарных типов данных, в частночти, картинок.

![image](https://user-images.githubusercontent.com/92520538/144826238-51e9631e-0bbb-446a-84cf-075518855bc2.png)

<!-- Docs to Markdown version 1.0β17 -->
