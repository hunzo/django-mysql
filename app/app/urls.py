from django.urls import path
from .views import Home, Update

urlpatterns = [
    path('', Home, name="home"),
    path('create/', Update, name="create")
]
