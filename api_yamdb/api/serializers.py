from rest_framework import serializers, exceptions
from reviews.models import User
from reviews.models import Category, Genre, Title
import datetime as dt
from reviews.models import Review, Comment


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError('Пользователь с таким именем '
                                              'не допустим. Пожалуйста '
                                              'выберите другое имя.')
        email = data['email']
        username = data['username']
        if (
           User.objects.filter(email=email).exists()
           or User.objects.filter(username=username).exists()):
            raise serializers.ValidationError(
                'Такой username или email уже существуют.'
            )
        return data


class UserTokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    def validate(self, data):
        username = data['username']
        confirmation_code = data['confirmation_code']
        if not User.objects.filter(username=username).exists():
            raise exceptions.NotFound('Пользователь не найден.')
        elif not User.objects.filter(
            confirmation_code=confirmation_code
        ).exists():
            raise serializers.ValidationError('Неправильный код')
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role',
        )


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
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        required=False,
        many=True,
        slug_field='slug'
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        required=False,
        slug_field='slug',
    )

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'category', 'genre')

    def validate_year(self, value):
        thisyear = dt.date.today().year
        if not (thisyear - 500 < int(value) <= thisyear):
            raise serializers.ValidationError(
                'Проверьте год, он должен быть в пределах '
                f'{thisyear - 500} - {thisyear}')
        return value


class TitleSerializerView(TitleSerializer):
    genre = GenreSerializer(
        required=False,
        many=True,
    )
    category = CategorySerializer(
        required=False,
    )


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
