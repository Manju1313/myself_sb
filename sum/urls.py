from django.urls import path

from . import views


urlpatterns = [
    path('min',views.min, name='min'),
    path('index', views.index, name='index'),
    #path('add',views.add, name='add')


]