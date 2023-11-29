from django.contrib import admin
from django.urls import path, include
from mysite import views

app_name = 'books'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('book/', views.BookList.as_view(), name='book_list'),
    path('author/', views.AuthorList.as_view(), name='author_list'),
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),  # 수정: PublisherList로 변경
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),  # 수정: BookDetail로 변경
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),  # 수정: AuthorDetail로 변경
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),  # 수정: PublisherDetail로 변경

    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('books/', include('books.urls')),
]
