<!----- Conversion time: 1.115 seconds.


Using this Markdown file:

1. Cut and paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β17
* Wed Sep 18 2019 01:01:48 GMT-0700 (PDT)
* Source doc: https://docs.google.com/open?id=1sIorEva0JHPGjUlZBihoiGIootksj8HqQUjW8Vota0c
----->



## 1. Основы работы с СКВ в графическом режиме


### Цель работы

Познакомиться на практике с основными приемами работы в современных системах контроля версий.


### Задания для выполнения



1. Установить на компьютер графический клиент Git.
2. Создайте в своей домашней папке (или в любой другой на ваш выбор) каталог, который будет содержать файлы нового программного проекта.
3. Выберите тематику программы, которую собираетесь написать. Язык программирования и используемые инструменты разработки сейчас не важны.
4. Инициализируйте в этой директории репозиторий гит.

![image](https://user-images.githubusercontent.com/92520538/137455260-3e0db0b3-bd05-4074-aa67-0ca2dc1a82bf.png)

![image](https://user-images.githubusercontent.com/92520538/137455382-39aca77e-3046-4e6d-808a-d97ae8b23ba0.png)

5. Обратите внимание на появление в этой папке скрытой подпапки с названием .git. Если вы ее не видите, то скорее всего, у вас отключено отображение скрытых папок.

![image](https://user-images.githubusercontent.com/92520538/137455577-70b67e8b-4bc6-4410-b8a4-638e2dc1fe1b.png)

6. Создайте новый файл для исходного текста программы. Если вы используете программный фреймворк, инициализируйте его в рабочий каталог.
7. Напишите несколько строк вашей программы.
8. Добавьте файл с исходным текстом (несколько файлов, если необходимо) в индекс вашего репозитория. 

![image](https://user-images.githubusercontent.com/92520538/137455887-660dcf8f-78a6-410a-8111-dfb491908a04.png)

9. Совершите ваш первый коммит. Напишите осмысленное сообщение коммита.

![image](https://user-images.githubusercontent.com/92520538/137456310-c2c05c91-d178-41d2-9a5d-3fe81956f755.png)

10. Повторите несколько раз. Каждый раз, завершая определенный этап работы, выполняйте коммит и описывайте проделанные изменения в сообщении коммита.

![image](https://user-images.githubusercontent.com/92520538/137456511-11eb6933-cfb5-4aff-9107-127256d743dd.png)

![image](https://user-images.githubusercontent.com/92520538/137456616-3c885082-3ad0-4c6c-ab41-b45ded0bd028.png)

11. Просмотрите историю коммитов. Попробуйте перейти на один из прошлых коммитов. Вернитесь в актуальное состояние программы.

![image](https://user-images.githubusercontent.com/92520538/137456722-c7858123-1c54-498b-9a25-f4292c104b9f.png)

![image](https://user-images.githubusercontent.com/92520538/137456898-e6483539-ea44-4723-89b1-ba186b287571.png)

![image](https://user-images.githubusercontent.com/92520538/137456939-d23f60f1-5837-454c-8f0b-8840e697e151.png)


### Методические указания

Для выполнения лабораторной работы необходимо воспользоваться любым консольным клиентом системы контроля версий Git, подходящую для рабочей операционной системы. Для Windows подойдет, например, дистрибутив [git-scm](https://git-scm.com/). Этот же пакет включает в себя и консольную утилиту git, необходимую для выполнения следующих работ. Для Linux существует, например, пакет [Git Cola](https://git-cola.github.io/). 

Для написания сообщений коммита необходимо придерживаться следующего общепринятого правила: в первой строке сообщения следует кратко описать произведенные изменения; если необходимо подробное описание, состоящее из многих строк, то его приводят, отступив от первой строки одну пустую. Помните, что заголовок описания коммита - это то, что будете видеть вы и ваши коллеги в истории изменений проекта. 


### Контрольные вопросы



1. Опишите своими словами значение следующих терминов:
    1. рабочий каталог - каталог для которого ведется контроль версий
    2. репозиторий - каталог на сайте github
    3. коммит - сохранение изменений, то есть текущего состояния каталога
    4. ветка - цепочка изменений, коммитов
2. Ознакомьтесь с гайдом по выбранной  вами программе-клиенту Git.


### Дополнительные задания



1. Представьте, что вы начинаете большой раздел работы. Для изоляции изменений создайте новую ветку. Назовите ее, чтобы было понятно, что вы в ней будете делать. 

![image](https://user-images.githubusercontent.com/92520538/137458443-3dccff4e-835c-4c19-849b-1378bda6d80b.png)

2. Перейдите в новую ветку и сделайте несколько коммитов.

![image](https://user-images.githubusercontent.com/92520538/137458695-1dec1ce1-5767-4c2c-981a-2718bd2afb02.png)

3. Перейдите в основную ветку и обратите внимание на состояние рабочей директории. 
4. Создайте еще одну ветку для работы над другим направлением в вашей программе. Обычно так работают в команде, каждый участник в собственной ветке. Либо в ветках может идти параллельная работа над разными возможностями программы. В таком случае эти ветки называются тематическими.
5. Сделайте несколько коммитов во вновь созданную ветку.

![image](https://user-images.githubusercontent.com/92520538/137459010-209c955e-ec6f-4555-9d5a-1da8fa53e124.png)

6. Перейдите в основную ветку и слейте в нее первую тематическую ветку.

![image](https://user-images.githubusercontent.com/92520538/137459209-6c47a696-7172-4866-bd9c-a6c9c8dcda33.png)

7. Слейте в основную ветку вторую тематическую. Если возникли конфликты слияния, разрешите их и завершите слияние. 

![image](https://user-images.githubusercontent.com/92520538/137459235-53a5afa0-ce4b-46e2-9dc8-403549481c6c.png)

8. Удалите более не нужные тематические ветки. Обратите внимание в истории, что даже при удалении веток никакие коммиты не теряются.

![image](https://user-images.githubusercontent.com/92520538/137459404-ee071b12-274b-4d9e-b533-dfcdb03514fd.png)


## 2. Работа с Git в терминале


### Цель работы

На основе уже полученных знаний о принципах работы СКВ получить более глубокое представление о работе Git  при помощи команд терминала.


### Задания для выполнения



1. Выберите тематику программы, которую собираетесь написать. Создайте для нее рабочую директорию
2. Инициализируйте в рабочей директории репозиторий при помощи команды git init.
3. Выполните в репозитории команду git status. Проинтерпретируйте полученное сообщение.

![image](https://user-images.githubusercontent.com/92520538/137459784-63476d15-3dc2-49ee-8eb9-29104f6d281f.png)

4. Создайте файл для исходного текста программы. Выполните команду git status.

![image](https://user-images.githubusercontent.com/92520538/137459898-b1a780d9-be92-423d-b047-5a57b606ad61.png)

5. Добавьте созданный файл под версионный контроль при помощи команды git add. Еще раз выполните git status.

![image](https://user-images.githubusercontent.com/92520538/137459984-89f71a74-98d6-4156-9fca-de0d9449bc5d.png)

6. Сделайте начальный коммит при помощи команды git commit с опцией -m.

![image](https://user-images.githubusercontent.com/92520538/137460034-ff476453-dfbe-4d14-9251-1abdab82ab9a.png)

7. Сделайте еще несколько коммитов. Выполните команду git log для просмотра истории коммитов.

![image](https://user-images.githubusercontent.com/92520538/137460183-d58dcaaa-207c-4d60-9902-5806b1179525.png)

8. Сделайте так, чтобы при коммите измененные файлы автоматически добавлялись в коммит.
9. Добавьте еще несколько файлов с исходным текстом программы. 
10.  Добавьте все новые файлы под версионный контроль одной командой. 

![image](https://user-images.githubusercontent.com/92520538/137460340-ec3964fc-77f9-4669-8bfe-9208df20b08c.png)

11. На всех стадиях работы пользуйтесь командой git status.
12. Инициализируйте в рабочей директории виртуальное окружение (Если вы пишите не на Python, то можете инициализировать какой-либо программный фреймворк, либо начать работать в IDE, которая создает скрытую папку с настройками в рабочем каталоге).

![image](https://user-images.githubusercontent.com/92520538/137460976-239d3dff-a803-4c06-a6da-aae12cfb966e.png)

13. Добавьте созданную служебную папку в файл .gitignore. Проверьте, что они не добавляются в репозитории при добавлении новых файлов с исходным кодом. 

![image](https://user-images.githubusercontent.com/92520538/137460926-bcf47aec-17d5-4539-b209-43d4d14bc9ab.png)

14. Создайте новую тематическую ветку git branch. Перейдите в нее с помощью git checkout. Выведите на экран список всех веток.

![image](https://user-images.githubusercontent.com/92520538/137461064-f2d17412-8ec4-462e-adc7-53b248346766.png)

![image](https://user-images.githubusercontent.com/92520538/137461114-7a545cc7-cc14-4cbf-8c83-a8ca48e9621c.png)

15. Сделайте несколько коммитов в основную и тематическую ветки. 

![image](https://user-images.githubusercontent.com/92520538/137461704-180e84fe-e218-4ca2-b9d3-d4e349725afb.png)

![image](https://user-images.githubusercontent.com/92520538/137461764-f849ff30-2d3e-408e-9cc7-3a24b301e650.png)

16. Слейте изменения в основную ветку с помощью git merge. Если произошел конфликт слияния, разрешите его и завершите слияние с помощью git commit.

![image](https://user-images.githubusercontent.com/92520538/137461943-02ba939f-5474-4e46-ad35-b1cb67341e46.png)

![image](https://user-images.githubusercontent.com/92520538/137462107-fff05a52-7a28-420c-ad71-9d88aed41dae.png)


17. При получении в процессе разработки программы в стабильно работающем состоянии, слейте это состояние в основную ветку и добавьте к коммиту слияния пометку с номером релиза.


### Методические указания

Для работы в терминале изучите шпаргалки по основным командам git.

Главные команды, которые вам понадобятся это:

git init - создает репозиторий системы контроля версий в данной директории;

git add - добавляет указанный файл под версионный контроль;

git add . - добавляет все файлы текущей директории под версионный контроль;

git status - показывает состояние рабочей директории по сравнению с последним сохраненным состоянием:

git commit -m "(message)" - сохраняет текущее состояние рабочей директории как новое состояние (создает новый коммит); новый коммит получает сообщение, переданное как параметр;

git commit -am "(message)" - создает новый коммит и автоматически включает в него все изменившиеся отслеживаемые файлы;

git log - выводит историю коммитов репозитория;

git branch - показывает список веток репозитория;

git branch <branchname> - создает новую ветку на основе текущего состояния с переданным названием;

git checkout -b <branchname> - создает новую ветку и автоматически делает ее текущей;

git merge <branchname> - сливает изменения, сделанные в ветке с переданным названием в текущую;

git branch -d <branchname> - удаляет ветку с переданным названием;

git clone (repo URL) - клонирует удаленный репозиторий, находящийся по переданному адресу в текущую директорию; доступ обычно осуществляется по протоколам HTTP либо SSH;

git fetch - считывает изменения в удаленном репозитории, отсутствующие в локальной копии;

git pull - считывает новые изменения в удаленном репозитории и сливает их в соответствующие локальные ветки;

git push –all - отправляет изменения, сделанные в локальном репозитории в удаленный;


### Контрольные вопросы



1. Что такое удаленный репозиторий? репозиторий на сервере github
2. Где нужно вводить команды git? в терминале
3. Для чего нужны ветки в системах контроля веток? чтобы вести различную независимую работу в ветках
4. Как возникают конфликты слияния? если были сделаны изменения в одном и том же месте, которые логически может решить только администратор
5. Как разрешать конфликты слияния? Вручную отменяя и задавая нужные изменения


### Дополнительные задания



1. Ознакомьтесь с методологией разработки GitFlow.
2. Установите на свой компьютер инструментальное средство для работы с GitFlow.
3. Выполните основные задания лабораторной работы с использованием команд git-flow.


## 3. Работа с удаленными репозиториями и GitHub


### Цель работы

Освоить основные навыки работы с облачными и распределенными системами контроля версий, получить навыки работы с инструментальными средствами, обеспечивающими командную работу над разработкой ПО.


### Задания для выполнения



1. Зарегистрироваться на сайте github.com
2. Установить на компьютере программу Git
3. Форкнуть данный репозиторий в свой аккаунт

![image](https://user-images.githubusercontent.com/92520538/137463730-2251e31d-b914-41f3-9524-dcd8c876fbb4.png)

4. Склонировать созданный удаленный репозиторий в директорию ~/git/test

![image](https://user-images.githubusercontent.com/92520538/137464269-a0ba44f0-ba91-455a-9c7d-5216820ebc92.png)

5. На локальной машине пишем скрипт ~/git/test/backup.sh, с произвольным содержанием
6. Фиксируем скрипт в репозитории (делаем коммит)
7. Обновляем удаленный репозиторий репозиторий (делаем пуш)

![image](https://user-images.githubusercontent.com/92520538/137464656-2442db5f-d611-4f6c-961c-79db1fab0069.png)
   
8. Через текстовый редактор добавить любую новую строку с комментарием
9. Сделать коммит
   
![image](https://user-images.githubusercontent.com/92520538/137464853-b237e5e0-852d-49f0-a425-017481e3ebde.png)

10. Вности синтаксическую ошибку в скрипт
11. Сделать коммит ошибочного скрипта
   
![image](https://user-images.githubusercontent.com/92520538/137464905-8dbde8f5-edd0-4e35-b54f-c083d00f51ee.png)

12. Откатываем до последней рабочей версии
   
![image](https://user-images.githubusercontent.com/92520538/137465099-cbfa6abc-5d5b-41f2-92b4-7518f91c982e.png)

13. Просмотреть историю коммитов
   
![image](https://user-images.githubusercontent.com/92520538/137465183-a816c043-3fb1-44d9-961b-80a655c26dee.png)

15. Добавить несколько коммитов произвольного содержимого
16. Создать пулл реквест в данный репозиторий

![image](https://user-images.githubusercontent.com/92520538/137465261-272aedb7-b54f-42e9-a1e7-00860a35eebf.png)


### Контрольные вопросы



1. Зачем нужен облачный хостинг репозиториев?
2. Какими основными функциями обладает сайт github.com?
3. Как организовать командную работу над открытым проектом?


### Дополнительные задания



1. Дополнительно оценивается, если студент продемонстрирует работу с ветками в процессе написания более-сложного программного проекта (не менее трех файлов, двух веток, десяти коммитов, как минимум одно объединение).
2. Дополнительно оценивается демонстрация командной работы. Для этого нужно склонировать репозиторий другому члену команды и коммитить от своего имени. При отправке истории на удаленный сервер (push) на сайте будет отображаться общая история. При скачивании истории с сервера (pull) общая история будет отображаться на локальном компьютере.
3. Настройте работу с git вашей интегрированной среды разработки по выбору. Для работы с python рекомендуется использовать PyCharm. Выполните задания лабораторной работы в IDE используя встроенные средства работы с системами контроля версий.

<!-- Docs to Markdown version 1.0β17 -->
