from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # О проекте
    path('about/', views.about, name='about'),
    
    # Правила использования
    path('rules/', views.rules, name='rules'),
]