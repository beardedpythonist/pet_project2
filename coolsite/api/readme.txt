

инструкции по API:

http://127.0.0.1:8000/ + :

1) api/v1/artikel           =  чтения всего контента  (  или + <int:pk>  = отдельной статьи)
                                    /только для авторизованных пользователей
2) api/v1/comment-edit/1    =  редактирование   комментов только автором
3) api/v1/comment-del/1     =  удаление   комментов только автором
4) api/v1/token/            =  получение пары токенов 'refresh -access'
5) api/v1/token/refresh/   =   получение  refresh-токена
