from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('articles/<str:pk>/',views.article_detail,name='detail'),
    path('publish_article/',views.publish,name='publish'),
]