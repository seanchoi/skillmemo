from .forms import *
from memo.models import *
from django.http import JsonResponse
from django.shortcuts import render, redirect

def image_upload_first_section(request, user_id):
    form = PhotoForm(request.POST, request.FILES)
    if form.is_valid():
        image = form.save()
        image.user=user_id
        image.save()
        data = {'is_valid': True, 'name': image.files.name, 'url': image.files.url}
    else:
        data = {'is_valid': False}
    return JsonResponse(data)

def image_upload_second_section(request, user_id):
    form = PhotoForm02(request.POST, request.FILES)
    if form.is_valid():
        image = form.save()
        image.user=user_id
        image.save()
        data = {'is_valid': True, 'name': image.files.name, 'url': image.files.url}
    else:
        data = {'is_valid': False}
    return JsonResponse(data)

def image_upload_third_section(request, user_id):
    form = PhotoForm03(request.POST, request.FILES)
    if form.is_valid():
        image = form.save()
        image.user=user_id
        image.save()
        data = {'is_valid': True, 'name': image.files.name, 'url': image.files.url}
    else:
        data = {'is_valid': False}
    return JsonResponse(data)

# image seletion clear
def clear_images(request, user_id):
    for photo in Photos.objects.filter(user=user_id):
        photo.files.delete()
        photo.delete()
    return redirect(f'/{user_id}/newmemo/')

def clear_images02(request, user_id):
    for photo in Photos02.objects.filter(user=user_id):
        photo.files.delete()
        photo.delete()
    return redirect(f'/{user_id}/newmemo/')

def clear_images03(request, user_id):
    for photo in Photos03.objects.filter(user=user_id):
        photo.files.delete()
        photo.delete()
    return redirect(f'/{user_id}/newmemo/')