from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name = 'myapp'

urlpatterns = [ 

    path('',(views.index), name='index'),
    path('<int:id>/',           views.detail,     name='detail'),
    path('add/',                views.create_item,     name='item_form'),
    path('update/<int:pk>/',    views.UpdateItem.as_view(),     name='item_update_form'),
    path('delete/<int:pk>/',    views.delete_item,     name='item_confirm_delete'),

]

