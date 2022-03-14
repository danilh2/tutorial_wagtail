from email.mime import image
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from deportes.models import Deporte

'''
N.B. To see what icons are available for use in Wagtail menus and StreamField block types,
enable the styleguide in settings:

INSTALLED_APPS = (
   ...
   'wagtail.contrib.styleguide',
   ...
)

or see http://kave.github.io/general/2015/12/06/wagtail-streamfield-icons.html

This demo project includes the full font-awesome set via CDN in base.html, so the entire
font-awesome icon set is available to you. Options are at http://fontawesome.io/icons/.
'''
#https://docs.wagtail.org/en/stable/reference/contrib/modeladmin/indexview.html#modeladmin-list-display

class DeportesAdmin(ModelAdmin):
    model = Deporte
    search_fields = ('name')
    menu_icon = 'site'
    menu_order = 300

    list_display = ('name', 'year', 'image_tag')

class DeportesAdminGroup(ModelAdminGroup):
    menu_label = 'Deportes'
    menu_icon = 'site'
    menu_order = 300
    items = (DeportesAdmin, )

modeladmin_register(DeportesAdminGroup)
