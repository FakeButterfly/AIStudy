from django.contrib import admin
from django.urls import path, include
from GLP import views  # 导入new应用中的views模块

urlpatterns = [
    path('', views.index),						#通过url设置对应的映射
    path('ask/', views.ask),
]