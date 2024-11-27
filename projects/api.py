from .models import Anime
from rest_framework import viewsets, permissions
from .serializers import AnimeSerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AnimeSerializer
