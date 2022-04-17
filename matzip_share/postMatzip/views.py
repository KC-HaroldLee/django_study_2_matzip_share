from unicodedata import category, name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.urls import reverse

from django.core.handlers.wsgi import WSGIRequest # <-- 멍청한 IDE를 위해

# Create your views here.

def index(request:WSGIRequest):
    categories = models.Category.objects.all()
    matzips = models.Matzip.objects.all()
    content = {'categories' : categories, 'matzips' : matzips}
    # return HttpResponse("index!")
    return render(request, 'postMatzip/index.html', content)

def matzipDetail(request:WSGIRequest, res_id:str):
    matzip = models.Matzip.objects.get(id=res_id)
    content = {'matzip' : matzip}
    # return HttpResponse("matzipDetail!")
    return render(request, 'postMatzip/matzipDetail.html', content)

def update_mat_page(request:WSGIRequest, res_id:str):
    categories = models.Category.objects.all()
    matzip = models.Matzip.objects.get(id=res_id)
    content = {'categories' : categories, 'matzip' : matzip}
    # return HttpResponse("matzipDetail!-"+res_id)
    return render(request, 'postMatzip/matzipUpdate.html', content)

def update_mat(request:WSGIRequest, res_id:str):
    pass

def matzipCreate(request:WSGIRequest):
    categories = models.Category.objects.all()
    content = {'categories' : categories}
    # return HttpResponse("matzipCreate!")
    return render(request, 'postMatzip/matzipCreate.html', content)

def create_mat(request:WSGIRequest):
    category_id = request.POST['resCategory'] # <input name 땜시...
    mat_category = models.Category.objects.get(id=category_id)
    mat_name = request.POST['resTitle']
    mat_link = request.POST['resLink']
    mat_content = request.POST['resContent']
    mat_loc = request.POST['resLoc']
    new_mat = models.Matzip(category = mat_category,
                            matzip_name=mat_name,
                            matzip_link=mat_link,
                            matzip_content=mat_content,
                            matzip_keyword=mat_loc
    
    )
    new_mat.save()
    # return HttpResponse("!?!??!?!")
    return HttpResponseRedirect(reverse('index'))

def categoryCreate(request:WSGIRequest):
    categories = models.Category.objects.all()
    content = {'categories' : categories}
    # return HttpResponse("categoryCreate")
    return render(request, 'postMatzip/categoryAdd.html', content)

def create_cate(request:WSGIRequest):
    # return HttpResponse("성공인가?")
    category_name = request.POST['categoryName']
    new_category = models.Category(category_name=category_name)
    new_category.save() # models.Model 에서 상속받은 함수 save()
    return HttpResponseRedirect(reverse('index'))

def delete_cate(request:WSGIRequest):
    category_id = request.POST['categoryId']
    print('>>>>>>>',category_id)
    delete_category = models.Category.objects.get(id = category_id)
    delete_category.delete() # models.Model 에서 상속받은 함수 save()
    return HttpResponseRedirect(reverse('categoryCreate'))