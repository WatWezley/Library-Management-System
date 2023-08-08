from django.urls import path, include
from book import views, views1
from rest_framework.routers import SimpleRouter, DefaultRouter

# router = SimpleRouter()
router = DefaultRouter()
router.register('author', views1.AuthorViewSet)
router.register('book', views1.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('send_mail/', views1.send_mail_function),
    path('sendmail/', views1.template_mail)
]

# urlpatterns = [
# path('', include(router.urls)),
# path('', include(router.urls)),
# path('author/', views1.AuthorList.as_view()),
# path('author/<int:pk>/', views1.AuthorDetails.as_view()),
# path('book/', views1.BookList.as_view()),
# path('book/<int:pk>/', views1.BookDetails.as_view()),

# path('authors/', views.list_authors, name='list_authors'),
# path('authors/<int:pk>/', views.author_detail, name='author_detail'),
# path('author/', views1.AuthorView.as_view()),
# path('author/<int:pk>/', views.author_detail, name='author_detail'),
# path('books/', views.book_list),
# path('books/<int:pk>/', views.book_detail)
# ]
