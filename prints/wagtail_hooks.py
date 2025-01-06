
from wagtail import hooks
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.images.models import Image
from .models import ArtisticPrint

class PrintAdmin(ModelAdmin):
    model = ArtisticPrint
    menu_label = 'Artistic Prints'
    menu_icon = 'tag'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name', 'payment_link')
    search_fields = ('name',)
    
modeladmin_register(PrintAdmin)