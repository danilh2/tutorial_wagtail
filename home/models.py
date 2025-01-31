from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    subpage_types = [
        'blog.BlogIndexPage', 
        'blog.ContactPage', 
        'pelis.PelisIndexPage', 
        'deportes.DeportesIndexPage',
    ]
    parent_page_type = [
        'wagtailcore.Page'
    ]