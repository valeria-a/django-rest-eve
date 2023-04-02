import django_filters
from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from movies_rest_app.models import Movie
from movies_rest_app.serializers import *


# api/imdb/movies - GET POST
# api/imdb/movies/movie_id - GET UPDATE DELETE


class MovieFilterSet(FilterSet):

    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')
    duration_from = django_filters.NumberFilter('duration_in_min', lookup_expr='gte')

    class Meta:
        model = Movie
        fields = ['name']


class MoviesViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilterSet
    # pagination_class = PageNumberPagination


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MovieDetailsSerializer
        else:
            return super().get_serializer_class()


    # movies/movie_id/actors
    # movies/actors
    @action(methods=['GET'], detail=True, url_path='actors')
    def movie_actors(self, request, pk):
        cast_qs = self.get_object().movieactor_set.all()
        serializer = CastWithActorNameSerializer(instance=cast_qs, many=True)
        return Response(data=serializer.data)