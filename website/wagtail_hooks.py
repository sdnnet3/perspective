from wagtail import hooks
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.images.models import Image
from .models import ImageProduct

class ProductAdmin(ModelAdmin):
    model = ImageProduct
    menu_label = 'Products'
    menu_icon = 'tag'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name', 'price', 'image_orientation')
    search_fields = ('name', 'description')

# modeladmin_register(ProductAdmin)

