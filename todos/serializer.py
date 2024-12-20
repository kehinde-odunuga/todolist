from rest_framework.serializers import ModelSerializer
from todos.models import Todo


class TodoSerializer(ModelSerializer):

    class Meta:
        model = Todo
        fields = ('title', 'desc', 'is_complete')