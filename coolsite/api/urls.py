from django.urls import path, include
from rest_framework import routers
from api.views import ArtikelRead, IsOwnerOnly, IsOwnerOnlyDestroy


api_router = routers.SimpleRouter()
api_router.register(r'artikel', ArtikelRead)



urlpatterns = [path('v1/',  include(api_router.urls)),
               path('v1/comment-edit/<int:pk>', IsOwnerOnly.as_view()),
               path('v1/comment-del/<int:pk>', IsOwnerOnlyDestroy.as_view())
               ]

#    1) api/v1/artikel           =  чтения всего контента
#    2) api/v1/comment-edit/1    =  редактирование   комментов только автором
#    3) api/v1/comment-del/1     =  удаление   комментов только автором

