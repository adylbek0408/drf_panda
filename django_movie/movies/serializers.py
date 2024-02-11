from rest_framework import serializers

from .models import Movie, Review


class MovieListSerializer(serializers.ModelSerializer):
    """Список фильмов"""

    class Meta:
        model = Movie
        fields = ("title", "tagline", "category")


class ReviewsCreateSerializer(serializers.ModelSerializer):
    """Отзыв"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewsSerializer(serializers.ModelSerializer):
    """Отзыв"""

    class Meta:
        model = Review
        fields = ("name", "text", "children")


class MovieDetailSerializer(serializers.ModelSerializer):
    """Полный фильм"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    reviews = ReviewsCreateSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ("draft", )

