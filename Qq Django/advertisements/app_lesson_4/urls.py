from django.urls import path
from .views import lesson

urlpatterns = [
    path('lesson_4/', lesson),
]