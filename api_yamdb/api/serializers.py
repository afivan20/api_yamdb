from rest_framework import serializers, exceptions
from reviews.models import User


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)

    def validate(self, data):
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('Пользователь с таким email уже '
                                              'существует')
        elif data['username'] == 'me':
            raise serializers.ValidationError('Пользователь с таким именем '
                                              'не допустим')
        return data

class UserTokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    def validate(self, data):
        username = data['username']
        confirmation_code = data['confirmation_code']
        if not User.objects.filter(username=username).exists():
            raise exceptions.NotFound('Пользователь не найден.')
        elif not User.objects.filter(confirmation_code=confirmation_code).exists():
            raise serializers.ValidationError('Неправильный код')
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
        


