from django.urls import path
from rango import views # contains function index

app_name = "rango"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name = "about"),
]