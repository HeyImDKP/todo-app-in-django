from rest_framework.serializers import ModelSerializer
from .models import TodoData

class TodoSerializer(ModelSerializer):
    class Meta:
        model = TodoData
        fields = ['id', 'title', 'details', 'date', 'done', 'user']