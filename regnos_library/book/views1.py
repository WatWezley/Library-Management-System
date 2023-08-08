from email.mime import message

from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import library
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from templated_mail.mail import BaseEmailMessage

import book
from . import static
from .filter import AuthorFilter, BookFilter
from rest_framework.filters import SearchFilter
from .pagination import DefaultPagination
from .permissions import IsAdminOrReadOnly
from .serilaizer import AuthorSerializer, BookSerializer
from book.models import Author, Book
from django_filters.rest_framework import DjangoFilterBackend

from .static import images


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AuthorFilter
    search_fields = ['first_name', 'last_name']
    permission_classes = [IsAdminOrReadOnly]

    authentication_classes = []


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    permission_classes = [IsAdminUser]


def send_mail_function(request):
    try:
        # send_mail("library message", "your book order is now available", "Ovn@gmail.com", ["ojogamil.com"])
        notification = EmailMessage("library message", "WELCOME TO REGLIB", "watwez@gmail.com", ["lilvivgamil.com"])
        notification.attach_file('book/static/images/babies.jpg')
        notification.send(fail_silently=True)
    except BadHeaderError:
        pass
    return HttpResponse('ok')


def template_mail(request):
    try:
        message = BaseEmailMessage(template_name='book/email.html', context={'name': 'wez'})
        message.send(['watwez@gmail.com'])
    except BadHeaderError:
        pass
    return HttpResponse('your Message has been sent successfully')

# class AuthorList(ListCreateAPIView):
# queryset = Author.objects.all()
# serializer_class = AuthorSerializer


# class AuthorDetails(RetrieveUpdateDestroyAPIView):
# queryset = Author.objects.all()
# serializer_class = AuthorSerializer

# -------------------------------------------------------------------------------------------------------------------
# class BookList(ListCreateAPIView):
# queryset = Book.objects.all()
# serializer_class = BookSerializer


# class BookDetails(RetrieveUpdateDestroyAPIView):
# queryset = Book.objects.all()
# serializer_class = BookSerializer

# def get_queryset(self):
# return Author.objects.all()

# def get_serializer_class(self):
# return AuthorSerializer

# -------------------------------------------------------------------------------------------------------------------

# class AuthorView(APIView):

# def get(self, request):
# authors = Author.objects.all()
# serializer = AuthorSerializer(authors, many=True)
# return Response(serializer.data, status=status.HTTP_201_CREATED)

# def put(self, request, pk):
# author = get_object_or_404(Author, pk=pk)
# serializer = AuthorSerializer(author, data=request.data)
# serializer.is_valid(raise_exception=True)
# serializer.save()
# return Response("Details Updated.", status=status.HTTP_200_OK)

# def delete(self, request, pk):
# author = get_object_or_404(Author, pk=pk)
# author.delete()
# return Response(status=status.HTTP_204_NO_CONTENT)
