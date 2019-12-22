from django.urls import path
# from .models import Blog
from . import views
urlpatterns = [
    path('', views.allBlogs, name='allBlogs'),
    path('<int:blog_id>/',views.detail,name='detail')
]
