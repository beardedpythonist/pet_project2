from django.urls import path, include
from rest_framework import routers
from api.views import ArtikelRead, IsOwnerOnly, IsOwnerOnlyDestroy
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

api_router = routers.SimpleRouter()
api_router.register(r'artikel', ArtikelRead)

urlpatterns = [path('v1/', include(api_router.urls)),
               path('v1/comment-edit/<int:pk>', IsOwnerOnly.as_view()),
               path('v1/comment-del/<int:pk>', IsOwnerOnlyDestroy.as_view()),
               path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
               path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
               path('v1/token/verify/', TokenVerifyView.as_view(), name='token_verify')
               ]

#    1) api/v1/artikel           =  чтения всего контента  (  или + <int:pk>  = отдельной статьи) /только для авторизованных пользователей
#    2) api/v1/comment-edit/1    =  редактирование   комментов только автором
#    3) api/v1/comment-del/1     =  удаление   комментов только автором
#    4) api/v1/token/            =  получение пары токенов: 'refresh -access'
#    5) api/v1/token/refresh/   =  получение  refresh-токена
