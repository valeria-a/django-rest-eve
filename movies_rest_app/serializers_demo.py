import datetime

from django.core.validators import MaxValueValidator
from rest_framework import serializers
from rest_framework import validators
from rest_framework.exceptions import ValidationError

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

    # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'duration_in_min', 'release_year']
        kwargs = {'id': {'readonly': True}}


def before_curr_year(value):
    if value > datetime.date.today().year:
        raise serializers.ValidationError('Before curr year')

class CreateMovieRawSerializer(serializers.Serializer):

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(required=False)
    duration_in_min = serializers.FloatField()
    release_year = serializers.IntegerField(
        validators=[MaxValueValidator(2000), before_curr_year])

    def validate(self, attrs):
        if attrs.get('name') == attrs.get('description'):
            raise serializers.ValidationError('Name and description can not be equal', 'same_content')
        return super().validate(attrs)


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
