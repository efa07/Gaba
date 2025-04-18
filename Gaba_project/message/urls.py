from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_message, name='new_message'),
]