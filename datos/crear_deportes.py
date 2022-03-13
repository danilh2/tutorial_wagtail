'''
crear deportes

ejecutar:

python manage.py shell < datos/crear_deportes.py
'''

from deportes.models import Deporte
from django.utils.text import slugify
import json
import os


# borrar deportes
for d in Deporte.objects.all():
    d.delete()

#lista de deportes del json
if os.path.exists("datos/datos_deportes.json"):
    deportes = json.load(open("datos/datos_deportes.json"))
else:
    deportes = json.load(open("datos_deportes.json"))

for d1 in deportes:
    d = Deporte()
    d.title = d1["name"]
    d.link = d1["url"]
    year = d1["year"]
    if year.isdigit():
        d.year = d1["year"]
    else:
        d.year = 0
    d.imagen = p1["img"]
    d.slug = slugify(f'{p.title}')
    d.save()
