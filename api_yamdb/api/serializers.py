from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from django.core.exceptions import ValidationError
from reviews.models import Category, Genre, Title, GenreTitle


class CategorySerializer(serializers.ModelSerializer):
    lookup_field = 'slug'

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    lookup_field = 'slug'

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    # genre = GenreSerializer(read_only=True, many=True)
    # category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, required=False,)
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        required=False,
        slug_field='name')

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'category', 'genre')

    # def create(self, validated_data):
    #     if 'tag' not in self.initial_data:
    #         post = Post.objects.create(**validated_data)
    #         return post
    #     tags = validated_data.pop('tag')
    #     post = Post.objects.create(**validated_data)
    #     for tag in tags:
    #         current_tag, status = Tag.objects.get_or_create(
    #             **tag)
    #         TagPost.objects.create(
    #             tag=current_tag, post=post)
    #     return post
