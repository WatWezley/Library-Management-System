from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serilaizer import AuthorSerializer
from .serilaizer import BookSerializer

from book.models import Author, Book


@api_view(['GET', 'POST'])
def list_authors(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializers = AuthorSerializer(authors, many=True)
        return Response(serializers.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        deserializer = AuthorSerializer(data=request.data)
        deserializer.is_valid(raise_exception=True)
        deserializer.save()
        return Response("Success", status=status.HTTP_201_CREATED)


# This is used when you are using django, response.
# def list_authors(request):
# return HttpResponse ("ok")


@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, pk):
    # author = get_object_or_404(Author, pk=pk)
    author = Author.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = AuthorSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Details Updated", status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        if author.book_set.count() > 0:
            return Response({"error": "Author associated with a book cannot be deleted"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#
# def list_authors(request):
#     author = Author.objects.all()
#     return render(request, 'author-list.html', {'authors': author})


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializers = BookSerializer(books, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        deserializer = BookSerializer(data=request.data)
        deserializer.is_valid(raise_exception=True)
        deserializer.save()
        return Response("Success", status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    # book = get_object_or_404()
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response("Details Updated", status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
