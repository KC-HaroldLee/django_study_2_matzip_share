from unicodedata import category
from django.db import models

# Create your models here.
# 데이터베이스에 반영하는 명령어
# python manage.py makemigrations
# python manage.py migrate

# 데이터베이스에 접속하는 명령
# python manage.py dbshell

class Category(models.Model):
    category_name = models.CharField(max_length=50)

class Matzip(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=3) # 외래키 가져오기
    matzip_name = models.CharField(max_length=50)
    matzip_link = models.CharField(max_length=100)
    matzip_content = models.TextField()
    matzip_keyword = models.CharField(max_length=50)