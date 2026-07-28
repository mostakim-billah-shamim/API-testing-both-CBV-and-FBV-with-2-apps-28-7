from django.urls import path
from .views import *

urlpatterns = [
    path('book/', BookPage, name='book'),
    path('book/<int:id>/', BookPage, name='book_update'),

    path('store/', StorePage, name='store'),
    path('store/<int:id>/', StorePage, name='store_update'),
]