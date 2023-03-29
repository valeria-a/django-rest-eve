from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

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

# Option 1
# class AddCastSerializer(serializers.Serializer):
#
#     actor = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all())
#     salary = serializers.IntegerField()
#     main_role = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return MovieActor.objects.create(movie_id=self.context['movie_id'], **validated_data)


# Option 2
# class AddCastSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = MovieActor
#         fields = ['actor', 'salary', 'main_role']
#
#
#     def create(self, validated_data):
#         validated_data['movie'] = self.context['movie']
#         return super().create(validated_data)


# # Option 3
# class AddCastSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = MovieActor
#         fields = ['actor', 'salary', 'main_role', 'movie']
#         extra_kwargs = {'movie': {'write_only': True}}


class AddCastSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieActor
        fields = ['actor', 'salary', 'main_role', 'movie']
        extra_kwargs = {'movie': {'write_only': True}}
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=MovieActor.objects.all(),
                fields=['movie', 'actor']
            )
        ]

    # def validate_salary(self, value):
    #     if value > 100_000_000:
    #         raise serializers.ValidationError('Way too much money for the role')
    #     return value


class CastWithActorNameSerializer(serializers.ModelSerializer):

    actor = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # Relationships must either set a queryset explicitly, or set read_only=True.

    class Meta:
        model = MovieActor
        exclude = ['movie', 'id']

