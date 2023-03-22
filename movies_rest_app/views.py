from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies_rest_app.models import *
from movies_rest_app.serializers import MovieSerializer


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
    query_set = Movie.objects.all()
    serializer = MovieSerializer(instance=query_set, many=True)
    return Response(serializer.data)