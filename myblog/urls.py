from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
 path("hakkimda", views.hakkimda_post_list, name="hakkimdalist"),
 path("", views.anasayfa, name="anasayfa"),
 path("hakkimda/detail/<int:pk>",views.hakkimda_detail, name="hakimda_detail"),
 path("blog",views.blog_index, name="blog"),
 path("blog/detail/<int:pk>", views.blog_detail,name="blogdetail")
]
