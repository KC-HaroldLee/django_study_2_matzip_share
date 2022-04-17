"""matzip_share URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('matzipDetail/<str:res_id>', views.matzipDetail, name='matzipDetail'), # 유동적인 <>
        path('matzipDetail/updatePage/<str:res_id>', views.update_mat_page, name='update_mat_page'), 
        path('matzipDetail/updatePage/update', views.update_mat, name='update_mat'), 
    path('matzipCreate/', views.matzipCreate, name='matzipCreate'),
        path('matzipCreate/create', views.create_mat, name='create_mat'),
    path('categoryCreate/', views.categoryCreate, name='categoryCreate'),
        path('categoryCreate/create', views.create_cate, name='create_cate'),
        path('categoryCreate/delete', views.delete_cate, name='delete_cate'),
]


