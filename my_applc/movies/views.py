from django.db import models
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend


from .models import Actor, Movie
from .serializers import (
    MovieListSerializer, 
    MovieDetailSerializer, 
    ReviewCraeteSerializer,
    CreateRatingSerializer,
    ActorListSerializer,
    ActorDetailSerializer,
    )
from .service import get_client_ip, MovieFilter



class MovieListView(generics.ListAPIView):
    """Вывод списка фильмов"""
    serializer_class = MovieListSerializer
    filtr_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings", 
                                    filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F("ratings__star")) / models.Count(models.F("ratings"))
        )
        return movies


class MovieDetailView(generics.RetrieveAPIView):
    """Вывод фильма"""
    queryset = Movie.objects.filter(draft=False)
    serializer_class = MovieDetailSerializer



class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзывов к фильму"""
    serializer_class = ReviewCraeteSerializer
        

class AddStarRatingView(generics.CreateAPIView):
    """Добавление рейтинга к фильму"""
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))



class ActorsListView(generics.ListAPIView):
    """Вывод списка актеров и режисеров"""
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorDetailView(generics.RetrieveAPIView):
    """Вывод актера или режисера"""
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
