from rest_framework import serializers

from core.authentication.serializers import UserReadSerializer, UserWatchlist
from core.recommendation.models import Genre, Movie, Watchlist


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieWriteSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True
                                                , queryset=Genre.objects.all())
    class Meta:
        model = Movie
        fields = '__all__'

class MovieReadSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

class WatchListWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ['movie']

    def create(self, validated_data):
        request = self.context.get('request')

        return Watchlist.objects.create(user=request.user, movie=validated_data.get('movie'))

class WatchListReadSerializer(serializers.ModelSerializer):
    user = UserWatchlist()
    movie = MovieReadSerializer()

    class Meta:
        model = Watchlist
        fields = '__all__'