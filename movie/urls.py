from django.urls import path
from .views import UpcomingMoviesList, MovieListCreate, MovieDetail

urlpatterns = [
    path('upcoming/', UpcomingMoviesList.as_view()),
    path('', MovieListCreate.as_view()),
    path('<int:pk>/', MovieDetail.as_view()),
]