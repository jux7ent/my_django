from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.templatetags.static import static

import os

def get_img_names(folder_name):
    images = []

    path = os.getcwd() + '/media/images/' + folder_name
    for file in os.listdir(path):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            images.append(file)

    return images


def some_func(request):
    return HttpResponse("Hello world")

def detail(request, folder_name):
    template = loader.get_template('imager/index.html')
    images = get_img_names(folder_name)
    context = {
        'folder_name': folder_name,
        'images': images,
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
