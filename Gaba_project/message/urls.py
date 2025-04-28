from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('msg/<int:item_pk>/', views.msg, name='new'),
]