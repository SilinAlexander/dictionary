from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView
from .models import Word, Category, Level, Theme
from .serializers import CategorySerializer, LevelSerializer, ThemeSerializer, ThemeRetrieveSerializer, WordSerializer
from rest_framework.views import View
from .permissions import HasAPISecret
from .filters import ThemeFilter
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class CategoryAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class LevelAPIView(ListCreateAPIView):
    serializer_class = LevelSerializer

    def get_queryset(self):
        return Level.objects.all()


class ThemeAPIView(ListAPIView):
    serializer_class = ThemeSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ThemeFilter

    def get_queryset(self):
        return Theme.objects.all()


class ThemeRetrieveAPIView(RetrieveAPIView, ThemeAPIView):
    serializer_class = ThemeRetrieveSerializer


class WordRetrieveAPIView(RetrieveAPIView):
    serializer_class = WordSerializer

    def get_queryset(self):
        return Word.objects.all()