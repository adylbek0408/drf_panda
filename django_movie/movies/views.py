from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie, Review
from .serializers import MovieListSerializer, MovieDetailSerializer, ReviewsCreateSerializer


class MovieListView(APIView):
    """Вывод списка фильмов"""
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    """Вывод фильмов"""
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    """Отзыв"""
    def post(self, request):
        review = ReviewsCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)
