import pytest
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestBookEndPoint:

    def test_that_user_cannot_get_book(self):
        client = APIClient()
        response = client.get('/library/book/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_that_anonymous_user_cannot_create_book(self):
        client = APIClient()
        response = client.post('/library/book/',
                               {"title": "a", "genre": "LIT", "isbn": "45654", "price": 456, "author": 56})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_that_admin_user_can_create_book(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.get('/library/book/')
        assert response.status_code == status.HTTP_200_OK

    def test_that_admin_get_404_with_invalid_data(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/library/book/', {"title": "a", "genre": "C",
                                                  "isbn": "916846781-345", "price": 456, "author": 56})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_that_admin_get_201_with_right_book_info(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/library/book/', {"title": "a", "genre": "FIN",
                                                  "isbn": "916846781-345", "price": 456, "author": 56})
        assert response.status_code == status.HTTP_200_OK
