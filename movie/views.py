from rest_framework import generics, filters
from .models import Movie
from .serializers import MovieSerializer

# 🎬 Upcoming Movies
class UpcomingMoviesList(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.filter(is_upcoming=True).order_by('release_date')


# 📌 List + Create
class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all().order_by('-created_at')
    serializer_class = MovieSerializer

    # 🔍 Search
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre', 'language']


# 📌 Detail (GET, PUT, DELETE)
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer