from django.urls import path
from .views import HomePageView
from .views import CategoryAPIView, LevelAPIView, ThemeAPIView, ThemeRetrieveAPIView, WordRetrieveAPIView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('levels/', LevelAPIView.as_view(), name='levels'),
    path('themes/', ThemeAPIView.as_view(), name='themes'),
    path('themes/<pk>/', ThemeRetrieveAPIView.as_view(), name='theme_retrieve'),
    path('words/<pk>/', WordRetrieveAPIView.as_view(), name='words'),
]
