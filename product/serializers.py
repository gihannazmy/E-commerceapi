from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(method_name='get_review',read_only=True)

    class Meta:
        model=Product
        fields = "__all__"

    def get_review(self,obj):
        reviews = obj.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model=Review
        fields = "__all__"