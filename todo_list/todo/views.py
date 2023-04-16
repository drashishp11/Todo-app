from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Tasks_todo
#from threading import Thread
#from django.core.mail import send_mail
#from django.conf import settings


# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Tasks_todo.objects.all()
