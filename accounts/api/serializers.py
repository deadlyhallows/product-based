from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import Q
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)

User = get_user_model()

class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'email2',
            'password',

        )
        extra_kwargs = {'password':
                            {'write_only': True}
                        }

    # def validate(self, data):
    #
    #     email = data['email']
    #     user = User.object.filter(email=email)
    #     if user.exists():
    #         raise ValidationError("user already exists")
    #     return data

    def validate_email(self, value):
        data = self.initial_data
        email2 = data['email2']
        email = value
        user = User.objects.filter(email=email)
        if user.exists():
            raise ValidationError("user already exists")
        if email != email2:
            raise ValidationError("Email must match")
        return value

    def validate_email2(self, value):
        data = self.initial_data
        email = data['email']
        email2 = value
        if email != email2:
            raise ValidationError("Email must match")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            email=email, username=username
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

