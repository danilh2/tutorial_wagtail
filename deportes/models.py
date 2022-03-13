from django.db import models

from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.snippets.models import register_snippet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify

class Deporte(models.Model):
    name = models.CharField('name', max_length=250)
    slug = models.SlugField(blank=True, max_length=250)
    link = models.URLField()
    year = models.IntegerField()
    imagen = models.URLField(max_length=250)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('link'),
        FieldPanel('year'),
        FieldPanel('imagen'),
    ]

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Deporte'
        verbose_name_plural = 'Deportes'
        

class DeportesIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, peliculas, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(deportes, 4)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        context = super().get_context(request)

        context['deportes'] = self.paginate(request, deportes)
        
        return context

    parent_page_types = ['home.HomePage']
    subpage_types = []
