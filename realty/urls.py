from django.urls import path

from . import views

urlpatterns = [
    path('', views.realty_news, name='realty_news'),
]