from django.db import models

from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.snippets.models import register_snippet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify

class Viaje(models.Model):
    year = models.IntegerField()
    date = models.DateField('fecha')
    name = models.CharField('nombre', max_length=250)
    desc = RichTextField(blank=True)
    doc = models.URLField()

    panels = [
        FieldPanel('year'),
        FieldPanel('date'),
        FieldPanel('name'),
        FieldPanel('desc'),
        FieldPanel('doc')
    ]
    def __str__(self):
        return f'{self.year} ({self.date} {self.name})'
    
    class Meta:
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'