from decimal import Decimal
from rest_framework import serializers
from book.models import Author, Book
from djoser.serializers import UserSerializer as CurrentUserCreateSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

# class AuthorSerializer(serializers.Serializer):
# first_name = serializers.CharField(max_length=255)
# last_name = serializers.CharField(max_length=255)
# date_of_birth = serializers.DateField()
from unicodedata import decimal


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


# class BookSerializer(serializers.Serializer):
# title = serializers.CharField(max_length=255)
# description = serializers.CharField(max_length=255)
# book_number = serializers.CharField(max_length=13, source='isbn')
# author = serializers.CharField(max_length=255)
# genre = serializers.CharField(max_length=15)


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'book_number', 'description', 'genre', 'price', 'discount_price', 'author']
        # fields = '__all__'

    # author = serializers.HyperlinkedRelatedField(
    # queryset=Author.objects.all(),
    # view_name='author_detail'
    # )

    book_number = serializers.CharField(max_length=13, source='isbn')
    discount_price = serializers.SerializerMethodField(method_name='calculate')

    def calculate(self, price: Book):
        return price.price * Decimal(0.1)


class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class CurrentUserSerializer(CurrentUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
