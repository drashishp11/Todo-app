from rest_framework import serializers
from .models import Tasks_todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks_todo
        fields = ('id', 'task', 'task_description', 'deadline', 'completed')
