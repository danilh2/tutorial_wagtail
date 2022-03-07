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
    slug = models.SlugField(blank=True, max_length=250)
    desc = RichTextField(blank=True)
    doc = models.URLField()

    panels = [
        FieldPanel('year'),
        FieldPanel('date'),
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('desc'),
        FieldPanel('doc')
    ]
    def __str__(self):
        return f'{self.year} ({self.date} {self.name})'
    
    class Meta:
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'

class ViajesIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, viajes, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(viajes, 10)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        qs = ''
        viajes = Viaje.objects.all().order_by('-date')

        context['viajes'] = self.paginate(request, viajes)
        context['qs'] = qs
        
        return context
