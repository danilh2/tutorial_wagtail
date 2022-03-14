'''
crear deportes

ejecutar:

python manage.py shell
cd datos
%run crear_deportes.py
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
    deportes = json.load(open("datos/datos_deportes.json", encoding="utf8"))
else:
    deportes = json.load(open("datos_deportes.json", encoding="utf8"))

for d1 in deportes:
    d = Deporte()
    d.name = d1["name"]
    d.link = d1["url"]
    year = d1["year"]
    if year.isdigit():
        d.year = d1["year"]
    else:
        d.year = 0
    d.imagen = d1["img"]
    d.slug = slugify(f'{d.name}')
    d.save()
