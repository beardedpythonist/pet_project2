# pet_project2


Привет. Меня зовут Гордей Александр,
я - python разработчик.

Это мой первый пет-проект. Этот сайт создан с помощью следующих технологий:

Python
Django
Django REST framework
Html
CSS
Bootstrap
СУБД sqlite3
Simple JWT
На сайте реализованы такие возможности как: регистрация/авторизация, пагинация, разделение записей по категориям, вывод отдельной статьи на новой странице, добавление коммментариев, поиск по сайту.
Также реализовано API с аутентификацией по технологии JWT token Bearer (библиотека Simple JWT).  

Инструкция по API: http://127.0.0.1:8000/ + :
1) api/v1/artikel = чтения всего контента (или + '/int' = отдельной статьи) /только для авторизованных пользователей
2) api/v1/comment-edit/1 = редактирование комментов только автором
3) api/v1/comment-del/1 = удаление комментов только автором
4) api/v1/token/ = получение пары токенов 'refresh -access'
5) api/v1/token/refresh/ = получение refresh-токена
