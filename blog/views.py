from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def postDetails(request, post_id):
    return render(request, 'blog/detail.html')

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url.'))

def new_url(request):
    return HttpResponse('This is new url')

def product_list(request):
    data = list(Product.objects.values())
    return JsonResponse(data, safe=False)