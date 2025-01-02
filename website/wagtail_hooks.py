from wagtail import hooks
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import Product  # Ensure this import is here

class ProductAdmin(ModelAdmin):
    model = Product
    menu_label = 'Products'
    menu_icon = 'tag'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name', 'price', 'stock', 'is_digital')
    search_fields = ('name', 'description')

modeladmin_register(ProductAdmin)
