from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name='home'),
    path('article/<int:id>', views.article), 
    path("article/<int:id>/edit", views.modify_article, name='article.edit'),
    path('article/<int:id>/update', views.update_article)

]