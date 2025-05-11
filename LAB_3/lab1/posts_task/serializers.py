from multiprocessing import Value
from .models import Post, Author
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    # def get_id(self, obj):
    #     return obj.pk
    # not needed ^

    class Meta:
        model = Post
        fields = ['id', 'title', 'content']

    def validate_title(self,value):
        if not value.isalpha():
            raise serializers.ValidationError('title should contain letters only !')
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # def get_id(self, obj):
    #     return obj.pk

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email']

    def validate_first_name(self,value):
        if not value.isalpha():
            raise serializers.ValidationError('first name should contain letters only !')
        return value
    
    def validate_last_name(self,value):
        if not value.isalpha():
            raise serializers.ValidationError('last name should contain letters only !')
        return value

    def validate_phone_number(self,value):
        if not value.isdigit():
            raise serializers.ValidationError('phone number should contain numbers only !')
        return value