from django.urls import path
from onepage import views

urlpatterns = [
    path('', views.index, name="index"),
]
