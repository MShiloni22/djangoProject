from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('input_processor', views.input_processor, name='input_processor')
]