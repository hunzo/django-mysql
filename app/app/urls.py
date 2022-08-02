from django.urls import path
from .views import Home, Create, Update, Delete

urlpatterns = [
    path('', Home, name="home"),
    path('create/', Create, name="create"),
    path('update/<int:pk>', Update, name="update"),
    path('delete/<int:pk>', Delete, name="delete"),
]
