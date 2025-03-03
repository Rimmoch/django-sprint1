from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),

    # Просмотр одного поста
    path('posts/<int:id>/', views.post_detail, name='post_detail'),

    # Посты по категориям
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
]