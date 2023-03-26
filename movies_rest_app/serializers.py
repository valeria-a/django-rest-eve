from django.core.validators import MaxValueValidator
from rest_framework import serializers
from rest_framework import validators

from movies_rest_app.models import *


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        exclude = ['birth_year']


class DetailedActorSerializer(serializers.ModelSerializer):

    model = ''
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    # actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ['actors', 'description']
        # fields = '__all__'
        # depth = 1
        # fields = ['id', 'name', 'release_year']


class MovieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['actors']


class CreateMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'duration_in_min', 'release_year']


# class ActorRawSerializer(serializers.Serializer):
#
#     def update(self, instance, validated_data):
#         pass
#
#     def create(self, validated_data):
#         pass
#
#     name = serializers.CharField()
#     birth_year = serializers.IntegerField(validators=[MaxValueValidator(2000)])
#     movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())


class CastSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieActor
        exclude = ['movie', 'id']
        depth = 1
