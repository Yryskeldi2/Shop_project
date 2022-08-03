from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewset, CommentViewSet, toggle_like, add_rating

router = DefaultRouter()
router.register("products", ProductViewset)
router.register("categories", CategoryViewSet)
router.register("comments", CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('toggle_like/<int:p_id>/', toggle_like),
    path('add_rating/<int:p_id>/', add_rating),

    
]