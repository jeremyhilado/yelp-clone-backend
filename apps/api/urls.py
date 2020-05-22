from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from apps.api.views import (
    BusinessViewSet, ReviewViewSet, PublicBusinesses, PublicBusinessDetail,
    PublicReviews, PublicReviewDetail, SearchDatabase, ImageViewSet
)
router = DefaultRouter()
router.register('businesses', BusinessViewSet, basename='businesses')
router.register('reviews', ReviewViewSet, basename='reviews')
router.register('images', ImageViewSet, basename='images')

custom_urlpatterns = [
    url(r'public-businesses/$', PublicBusinesses.as_view(), name='public_businesses'),
    url(r'public_businesses/(?P<pk>\d+)/$', PublicBusinessDetail.as_view(), name='public_business_detail'),
    url(r'public-reviews/$', PublicReviews.as_view(), name='public_reviews'),
    url(r'public-reviews/(?P<pk>\d+)/$', PublicReviewDetail.as_view(), name='public_review_detail'),
    url(r'search/$', SearchDatabase.as_view(), name='search')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
