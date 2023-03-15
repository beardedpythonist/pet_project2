from rest_framework.generics import RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from women.models import Women, Comments
from api.serializer import ArtikelSerializer, CommentSerializer
from api.permissions import IsOwnerOrReadOnly


class ArtikelRead(ReadOnlyModelViewSet):
    queryset = Women.objects.all()
    serializer_class = ArtikelSerializer
    permission_classes = (IsAuthenticated, )


class IsOwnerOnly(RetrieveUpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    # взял код из документации и  создал свой  пермишн https://www.django-rest-framework.org/api-guide/permissions
    # permission_classes = (IsOwnerOrReadOnly,) пермишшн позволяет редактировать и удалять комментарии только их автору


class IsOwnerOnlyDestroy(RetrieveDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

