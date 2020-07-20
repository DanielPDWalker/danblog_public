from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:post_slug>', views.post, name='post'),
    path('tag/', views.tag, name='tag'),
    path('tag/<str:tag_string>', views.tag_search, name ='tag_search')
]
