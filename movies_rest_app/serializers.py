from rest_framework import serializers

from movies_rest_app.models import Movie, Actor


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


# class ActorSerializer(serializers.ModelSerializer):
#
#     name = serializers.CharField()
#     birth_year = serializers.IntegerField()
