"""postit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from apps.core.views import frontpage, signup
from apps.feed.views import feed, search
from apps.feed.api import api_add_post
from apps.postitprofile.views import postitprofile, follow_poster, unfollow_poster, followers, follows, edit_profile

urlpatterns = [
    ## admin
    path('admin/', admin.site.urls),

    path('', frontpage, name = 'frontpage'),
    path('signup/', signup, name = "signup"),
    path('logout/', views.LogoutView.as_view(), name = "logout"),
    path('login/', views.LoginView.as_view(template_name = 'core/login.html'), name = 'login'),


    ## main page here
    path('feed/', feed, name = 'feed'),
    path('search/', search, name = 'search'),
    path('u/<str:username>/', postitprofile, name = 'postitprofile'),
    path('u/<str:username>/follow/', follow_poster, name = 'follow_poster'),
    path('u/<str:username>/unfollow/', unfollow_poster, name = 'unfollow_poster'),
    path('u/<str:username>/followers/', followers, name = 'followers'),
    path('u/<str:username>/follows/', follows, name = 'follows'),
    path('edit_profile/', edit_profile, name = 'edit_profile'),

    ## API

    path('api/add_post/', api_add_post, name = 'api_add_post'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

