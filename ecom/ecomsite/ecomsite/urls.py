
from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('admin/', admin.site.urls),
    path('checkout/', views.checkout, name='checkout'),
]
