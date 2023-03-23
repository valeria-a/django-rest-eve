from django import shortcuts
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies_rest_app.models import *
from movies_rest_app.serializers import *


# Create your views here.

# @api_view(['GET'])
# def get_movies(request):
#     query_set = Movie.objects.all()
#     movies_list = []
#     for movie in query_set:
#         movies_list.append({
#             'id': movie.pk,
#             'name': movie.name,
#             'description': movie.description
#         })
#     return Response(movies_list)


@api_view(['GET'])
def get_movies(request):

    # get data from the DB
    movies_qs = Movie.objects.all()
    print(movies_qs.query)

    if 'name' in request.query_params:
        movies_qs = movies_qs.filter(name__iexact=request.query_params['name'])
        print(movies_qs.query)
    if 'duration_from' in request.query_params:
        movies_qs = movies_qs.filter(duration_in_min__gte=request.query_params['duration_from'])
        print(movies_qs.query)
    if 'duration_to' in request.query_params:
        movies_qs = movies_qs.filter(duration_in_min__lte=request.query_params['duration_to'])
        print(movies_qs.query)
    if 'description' in request.query_params:
        movies_qs = movies_qs.filter(description__icontains=request.query_params['description'])
        print(movies_qs.query)
    # if 'names_list' in request.query_params:
    #     names = request.query_params['names_list'].lower().split(",")
    #     movies_qs = movies_qs.filter(name__lower__in=names)
    #     print(movies_qs.query)

    serializer = MovieSerializer(instance=movies_qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_movie(request, movie_id):
    # try:
    #     movie = Movie.objects.get(id=movie_id)
    #     serializer = MovieDetailsSerializer(instance=movie, many=False)
    #     return Response(serializer.data)
    # except Movie.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieDetailsSerializer(instance=movie, many=False)
    return Response(serializer.data)
