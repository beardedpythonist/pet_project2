from rest_framework.serializers import ModelSerializer
from women.models import Women
from women.models import Comments


class ArtikelSerializer(ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Women
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Comments
        fields = '__all__'

