Реализовать простой чат сервер на базе сервера аутентификации. Сервер должен обеспечивать подключение многих пользователей одновременно, отслеживание имен пользователей, поддерживать историю сообщений и пересылку сообщений от каждого пользователя всем остальным.
Подключение многих пользователей, работа с каждым в отдельном потоке. ТАкже отслеживаются имена и пароли

![image](https://user-images.githubusercontent.com/92520538/137736100-5d48b9f8-1fb5-4655-a7b2-373ee9b7607e.png)

Сообщения пересылаются другим пользователям в таком виде

![image](https://user-images.githubusercontent.com/92520538/137736777-9d66d60a-3b83-4d41-a7f6-a019f4a27ecf.png)

![image](https://user-images.githubusercontent.com/92520538/137736795-ba937029-330b-4f06-80fc-7074112d67c3.png)

![image](https://user-images.githubusercontent.com/92520538/137736818-df7c21a7-56d5-41dc-8929-ff7af2951c55.png)

История хранится в файле history(time).txt

![image](https://user-images.githubusercontent.com/92520538/137736923-58f3f3cc-eb85-407d-bdcf-25976ccff447.png)

![image](https://user-images.githubusercontent.com/92520538/137736945-07691a49-ea68-462f-b76d-1caf3f1d6e97.png)

Логи пишутся в файл log.txt а логины пароли в файл logins.csv

![image](https://user-images.githubusercontent.com/92520538/137737067-57eb3d53-d683-4f46-a45f-46a74bc7fcb6.png)

![image](https://user-images.githubusercontent.com/92520538/137737143-33f0ef4f-c5d3-42df-81b5-9fa849601f71.png)

Реализовать сервер с управляющим потоком. При создании сервера прослушивание портов происходит в отдельном потоке, а главный поток программы в это время способен принимать команды от пользователя. Необходимо реализовать следующие команды:
Отключение сервера (завершение программы); по команде выкл

![image](https://user-images.githubusercontent.com/92520538/137738413-15f64320-fe8d-4cc0-9878-5e46cbafd25d.png)

Пауза (остановка прослушивание порта); по команде заморозить, разморозить

![image](https://user-images.githubusercontent.com/92520538/137737648-6d49d1dc-35e5-4ac8-9d7b-fb2c16fe71da.png)

Показ логов; по команде показывать не показывать

![image](https://user-images.githubusercontent.com/92520538/137738078-f6a9729a-870e-454a-9f61-1a9fce745033.png)

Очистка логов; командой очистить

![image](https://user-images.githubusercontent.com/92520538/137738185-5f993cce-c1e7-4994-8dd4-3762030637fc.png)

![image](https://user-images.githubusercontent.com/92520538/137738241-57ad0c72-2450-40f6-8c68-4b46c5267c8c.png)

Очистка файла идентификации. командой удалить клиентов

![image](https://user-images.githubusercontent.com/92520538/137738282-01ad87a0-8044-41a0-815c-61ca92d81d2b.png)

![image](https://user-images.githubusercontent.com/92520538/137738337-cb583bcd-70fc-4f3f-8432-d8ed12cf4aad.png)

