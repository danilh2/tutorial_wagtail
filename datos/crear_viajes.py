'''
crear viajes

ejecutar:

python manage.py shell < datos/crear_viajes.py
'''

from viajes.models import Viaje
from django.utils.text import slugify
import json
import os


# borrar viajes
for v in Viaje.objects.all():
    v.delete()

#lista de viajes del csv
if os.path.exists("datos/datos_viajes.csv"):
    viajes = json.load(open("datos/datos_viajes.csv"))
else:
    viajes = json.load(open("datos_viajes.csv"))


for v1 in viajes:
    v = Viaje()
    v.year = v1["Año"]
    v.date = v1["Fecha"]
    v.name = v1["Destino"]
    v.desc = v1["Descripción"]
    v.doc = v1["Documento"]
    v.slug = slugify(f'{v.year} ({v.date} {v.name})')
    v.save()
