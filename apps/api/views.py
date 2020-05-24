from rest_framework import generics, viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated
from .models import Business, Review, Image
from .serializers import BusinessSerializer, ReviewSerializer, ImageSerializer
from django.contrib.postgres.search import SearchVector


class BusinessViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Business.objects.all()
        return queryset

    serializer_class = BusinessSerializer

    def create(self, request):
        business = Business.objects.filter(
            name=request.data.get('name'),
            owner=request.user
        )
        if business:
            msg = 'Business with that name already exists.'
            raise ValidationError(msg)
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        business = Business.objects.get(pk=self.kwargs["pk"])
        if not request.user == business.owner:
            raise PermissionDenied("You do not have permission to delete this business.")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Review.objects.all()
        return queryset

    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        review = Review.objects.get(pk=self.kwargs["pk"])
        if not request.user == review.owner:
            raise PermissionDenied("You do not have permission to delete this review.")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Review.objects.all()
        return queryset

    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        image = Image.objects.get(pk=self.kwargs["pk"])
        if not request.user == image.owner:
            raise PermissionDenied("You do not have permission to delete this image.")
        return super().destory(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SearchDatabase(generics.ListAPIView):
    def get_queryset(self):
        search_term = self.request.GET.get('q',)
        queryset = Business.objects.annotate(search=SearchVector('name', 'categories', 'location_city', 'location_state',),).filter(search=search_term)
        return queryset

    serializer_class = BusinessSerializer


class BusinessEdit(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Business.objects.all().filter(owner=self.request.user)
        return queryset

    serializer_class = BusinessSerializer


class ReviewEdit(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Review.objects.all().filter(owner=self.request.user)
        return queryset

    serializer_class = ReviewSerializer


class ImageEdit(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Image.objects.all().filter(owner=self.request.user)
        return queryset

    serializer_class = ImageSerializer
