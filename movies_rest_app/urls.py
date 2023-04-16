"""
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
from rest_framework import routers

from movies_rest_app import views
from movies_rest_app.views_generics import MoviesViewSet

router = routers.DefaultRouter()
router.register(r'movies', MoviesViewSet, basename='movie')

urlpatterns = [
    # path('movies', views.movies),
    # path('movies/<int:movie_id>', views.get_movie),
    # path('movies/<int:movie_id>/actors', views.movie_actors),

    # path('movies', views.MoviesApiView.as_view())
]
urlpatterns.extend(router.urls)
print(urlpatterns)

# api/imdb/movies/abc