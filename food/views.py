from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from food.models import *


@csrf_exempt
def category_data(request):
    if request.method == 'GET':
        category_list = []
        category_queryset = Category.objects.all().order_by('-created')
        for category_obj in category_queryset:
            data = {}
            image = str(category_obj.image)
            if image is not '':
                image = request.scheme + '://' + request.get_host() + '/media/' + image
            else:
                image = ''
            data['category_id'] = category_obj.id
            data['category_name'] = category_obj.name
            data['category_image'] = image
            category_list.append(data)
        return JsonResponse({'success': True, 'category_list': category_list})


@csrf_exempt
def sub_category_data(request):
    if request.method == 'GET':
        category_id = request.GET.get('category_id')
        category_obj = Category.objects.get(id=int(category_id))
        sub_category_list = []
        sub_category_queryset = SubCategory.objects.filter(category=category_obj)
        for sub_category_obj in sub_category_queryset:
            data = {}
            image = str(sub_category_obj.image)
            if image is not '':
                image = request.scheme + '://' + request.get_host() + '/media/' + image
            else:
                image = ''
            data['sub_category_id'] = sub_category_obj.id
            data['sub_category_name'] = sub_category_obj.name
            data['sub_category_image'] = image
            data['sub_category_price'] = sub_category_obj.price
            sub_category_list.append(data)
        return JsonResponse({'success': True, 'sub_category_list': sub_category_list})


@csrf_exempt
def sub_category_image(request):
    if request.method == 'GET':
        sub_category_id = request.GET.get('sub_category_id')
        sub_category_obj = SubCategory.objects.get(id=int(sub_category_id))
        image_list = []
        image_queryset = SubCategoryImage.objects.filter(sub_category=sub_category_obj)
        for image_obj in image_queryset:
            data = {}
            image = str(image_obj.image)
            if image is not '':
                image = request.scheme + '://' + request.get_host() + '/media/' + image
            else:
                image = ''
            data['image_id'] = image_obj.id
            data['image_name'] = image_obj.name
            data['sub_category_image'] = image
            image_list.append(data)
        return JsonResponse({'success': True, 'sub_category_image_list': image_list})
