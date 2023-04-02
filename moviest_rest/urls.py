"""moviest_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from movies_rest_app.views import get_version

# api/ttt/users
# api/imdb/movies => movies/

from rest_framework import routers

from movies_rest_app.views_generics import MoviesViewSet

router = routers.DefaultRouter()
router.register(r'api/imdb/movies', MoviesViewSet, basename='movie')

# api/imdb/movies - GET -> MoviesViewSet.list
# api/imdb/movies - POST -> MoviesViewSet.create
# api/imdb/movies/<movie_id> - GET -> MoviesViewSet.retrieve

print("Simple router urls:", router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/imdb/', include('movies_rest_app.urls')),
    path('api/version', get_version)
]
urlpatterns.extend(router.urls)

print(urlpatterns)