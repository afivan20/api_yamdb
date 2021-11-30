from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from django.core.exceptions import ValidationError
from reviews.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, required=False)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'category', 'genre')


# class PostSerializer(serializers.ModelSerializer):
#     author = SlugRelatedField(slug_field='username', read_only=True)

#     class Meta:
#         fields = '__all__'
#         model = Post


# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.SlugRelatedField(
#         read_only=True, slug_field='username',)

#     class Meta:
#         fields = '__all__'
#         model = Comment


# class FollowSerializer(serializers.ModelSerializer):
#     user = serializers.SlugRelatedField(
#         slug_field='username',
#         queryset=User.objects.all(),
#         default=serializers.CurrentUserDefault())
#     following = serializers.SlugRelatedField(
#         slug_field='username',
#         queryset=User.objects.all())

#     class Meta:
#         model = Follow
#         fields = ('user', 'following')
#         validators = (
#             UniqueTogetherValidator(
#                 queryset=Follow.objects.all(),
#                 fields=('user', 'following', )
#             ),
#         )

#     def validate(self, data):
#         if data['user'] == data['following']:
#             raise ValidationError('You can\'t subscribe to sai yourself')
#         return data
