#from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Anime
from .serializers import AnimeSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

    def create(self, request, *args, **kwargs):
        print("Datos recibidos:", request.data)  # Para verificar los datos enviados
        return super().create(request, *args, **kwargs)
