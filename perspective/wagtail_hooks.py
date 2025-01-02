from wagtail import hooks
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import ClientLoginPage  # Add this import

@modeladmin_register
class ClientLoginPageAdmin(ModelAdmin):
    model = ClientLoginPage
    menu_label = 'Client Login'
    menu_icon = 'user'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False