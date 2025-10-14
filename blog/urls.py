from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.postDetails, name='post'),
    path('old_url', views.old_url_redirect, name='old_url'),
    path('new_url', views.new_url, name='new_page_url'),
    path('products/', views.product_list, name='product_list'),
]