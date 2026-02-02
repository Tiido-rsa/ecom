from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('register/',   views.register,             name='register'),
    path('login/',      auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',     views.logout_view,          name='logout'),
    path('profile/',    views.profile,              name='profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
