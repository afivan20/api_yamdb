from rest_framework import serializers
from reviews.models import Category, Genre, Title, GenreTitle
import datetime as dt


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
    genre = GenreSerializer(many=True, required=False,)
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        required=False,
        slug_field='name')

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'category', 'genre')

    def validate_year(self, value):
        thisyear = dt.date.today().year
        if not (thisyear - 500 < int(value) <= thisyear):
            raise serializers.ValidationError('Проверьте год!')
        return value

    def create(self, validated_data):
        if 'genre' not in self.initial_data:
            title = Title.objects.create(**validated_data)
            return title
        genres = validated_data.pop('genre')
        title = Title.objects.create(**validated_data)
        for genre in genres:
            current_genre, status = Genre.objects.get_or_create(**genre)
            GenreTitle.objects.create(
                genre=current_genre, title=title)
        return title
