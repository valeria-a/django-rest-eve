from rest_framework import serializers

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

    class Meta:
        model = Movie
        exclude = ['actors']
        extra_kwargs = {
            'id': {'read_only': True},
            'description': {'write_only': True, 'required': False}
        }

    # def validate(self, attrs):
    #     self.context['request']


class MovieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['actors']


class CastSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieActor
        exclude = ['movie', 'id']
        depth = 1
