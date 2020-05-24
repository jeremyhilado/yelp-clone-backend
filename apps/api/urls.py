from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from apps.api.views import (
    BusinessViewSet, ReviewViewSet, SearchDatabase, ImageViewSet,
    BusinessEdit, ReviewEdit, ImageEdit
)
router = DefaultRouter()
router.register('businesses', BusinessViewSet, basename='businesses')
router.register('reviews', ReviewViewSet, basename='reviews')
router.register('images', ImageViewSet, basename='images')

custom_urlpatterns = [
    url(r'businesses/(?P<pk>\d+)/$', BusinessEdit.as_view(), name='business-edit'),
    url(r'reviews/(?P<pk>\d+)/$', ReviewEdit.as_view(), name='review-edit'),
    url(r'images/(?P<pk>\d+)/$', ImageEdit.as_view(), name='image-edit'),
    url(r'search/$', SearchDatabase.as_view(), name='search')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
