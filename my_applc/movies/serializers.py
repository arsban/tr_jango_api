from rest_framework import serializers

from .models import (
    Movie, 
    Rating, 
    Review,
    Actor,
    )


class FilterReviewListSerializer(serializers.ListSerializer):
    
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ActorListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режисеров"""
    class Meta:
        model = Actor
        fields = ('id', 'name', 'image')


class ActorDetailSerializer(serializers.ModelSerializer):
    """Вывод полного описания актеров или режисеров"""
    class Meta:
        model = Actor
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'tagline', 'category', 'rating_user', 'middle_star')


class ReviewCraeteSerializer(serializers.ModelSerializer):


    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):

    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("name", "text", "parent")


class MovieDetailSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = ActorListSerializer(read_only=True, many=True)
    actors = ActorListSerializer(read_only=True, many=True)
    ganre = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    reviews = ReviewCraeteSerializer(many=True)
    class Meta:
        model = Movie
        exclude = ("draft", ) # exclude позволяет выводить все поля модели уроме того что в нее записан


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователей"""
    class Meta:
        model = Rating
        fields = ("star", "movie")

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            ip=validated_data.get("ip", None),
            movie=validated_data.get("movie", None),
            defaults={"star": validated_data.get("star")}
        )
        return rating