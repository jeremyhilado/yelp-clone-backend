from rest_framework import serializers
from apps.api.models import Business, Review, Image


class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Image
        fields = ('id', 'business', 'image_url', 'description', 'created_at', 'updated_at', 'owner', 'is_public')


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'business', 'rating', 'review', 'created_at',
                  'updated_at', 'owner', 'is_public')


class BusinessSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    reviews = ReviewSerializer(many=True, read_only=True, required=False, source='business_review')
    images = ImageSerializer(many=True, read_only=True, required=False, source='business_image')

    class Meta:
        model = Business
        fields = ('id', 'name', 'images', 'location_address', 'location_city', 'location_state',
                  'categories', 'price', 'website', 'phone', 'reviews', 'created_at', 'updated_at', 'owner',
                  'is_public')

