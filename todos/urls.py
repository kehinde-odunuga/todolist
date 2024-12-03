from django.urls import path
from todos.views import CreateTodoAPIView

urlpatterns = [
    path('create', CreateTodoAPIView.as_view(), 'create-todo')
]