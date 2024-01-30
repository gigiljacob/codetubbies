import os

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from core.settings import BASE_DIR
from utils.sent_email_template import send_email

User = get_user_model()


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(UserTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['name'] = user.name
        token['gender'] = user.gender
        token['company'] = user.company
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('i_am', 'name', 'email', 'password', 'gender', 'company', 'skills')
        extra_kwargs = {
            'i_am': {'required': True},
            'name': {'required': True},
            'email': {'required': True},
            'gender': {'required': True},
            'company': {'required': True},
            'skills': {'required': True},
        }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})
    #
    #     return attrs

    def create(self, validated_data):
        user = User.objects.create(
            i_am=validated_data['i_am'],
            name=validated_data['name'],
            email=validated_data['email'],
            gender=validated_data['gender'],
            company=validated_data['company'],
            skills=validated_data['skills']
        )

        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()

        subject = "Welcome to TechGig.com! Please verify your email ID"
        template = os.path.join(BASE_DIR, 'email_templates')
        send_email(subject, user.email, template)

        return user
