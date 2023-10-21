from django.urls import path 
# from films.views import FilmListAPIView, FilmDetailAPIView
from films.views import FilmViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('films', FilmViewSet, basename='films')
urlpatterns = router.urls


# urlpatterns = [
#     path('films/', FilmListAPIView.as_view()), 
#     path('films/<int:pk>/', FilmDetailAPIView.as_view()) 
# ]