from rest_framework import viewsets

from core.recommendation.models import Genre, Movie, Watchlist, Review
from core.recommendation.serializers import GenreSerializer, MovieWriteSerializer, MovieReadSerializer, \
    WatchListWriteSerializer, WatchListReadSerializer, ReviewSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.order_by('id')
    serializer_class = GenreSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.order_by('id')
    write_serializer_class = MovieWriteSerializer
    read_serializer_class = MovieReadSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return self.read_serializer_class
        return self.write_serializer_class

class WatchListViewSet(viewsets.ModelViewSet):
    queryset = Watchlist.objects.order_by('id')
    write_serializer_class = WatchListWriteSerializer
    read_serializer_class = WatchListReadSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return self.read_serializer_class
        return self.write_serializer_class

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.order_by('id')
    serializer_class = ReviewSerializer