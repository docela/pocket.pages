from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books'),
    path('<int:book_id>', views.book, name='book'),
    path('search', views.search, name='search'),
    path('add', views.add, name='add'),
    path('statistics', views.statistics, name='statistics'),
]
