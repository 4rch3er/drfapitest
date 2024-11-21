import json
from django.core.management.base import BaseCommand
from projects.models import Anime  # Cambia a la ruta correcta

class Command(BaseCommand):
    help = 'Carga datos de un archivo JSON a la base de datos'

    def handle(self, *args, **kwargs):
        file_path = r'C:\Users\takes\OneDrive\Escritorio\BACK UP - NOTE\DRF\todos_los_animes.json'  # Ajusta la ruta
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                Anime.objects.create(
                    titulo=item['Titulo'],
                    tipo_anime=item['Tipo_Anime'],
                    episodios=item['Episodios'],
                    url=item['URL'],
                    fecha=item['Fecha'],
                    estado=item['Estado'],
                    generos=item['Generos'],
                    sinopsis=item['Sinopsis'],
                )

        self.stdout.write(self.style.SUCCESS('Datos importados con éxito'))
