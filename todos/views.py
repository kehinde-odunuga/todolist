from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from todos.serializer import TodoSerializer
from rest_framework.permissions import IsAuthenticated



class CreateTodoAPIView(CreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)