from coderedcms import admin_urls as crx_admin_urls
from coderedcms import search_urls as crx_search_urls
from coderedcms import urls as crx_urls
from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from wagtail.documents import urls as wagtaildocs_urls

from perspective.api import api
from perspective.views import subscribe
from .views import ClientLoginView, cart_add, cart_remove, cart_detail
from website.views import product_list, artistic_prints_list

urlpatterns = [
    # Admin
    path("django-admin/", admin.site.urls),
    path("admin/", include(crx_admin_urls)),
    
    #api
    path('api/', api.urls),

    # Client-login
    path('login/', ClientLoginView.as_view(), name='client_login'),

    # Cart
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('cart/', cart_detail, name='cart_detail'),

    # mailchimp
    path('subscribe/', subscribe, name='subscribe'),

    # Product list
    path('products/', product_list, name='product_list'),
    path('prints/', artistic_prints_list, name='artistic_prints_list'),

    # Documents
    path("docs/", include(wagtaildocs_urls)),
    # Search
    path("search/", include(crx_search_urls)),
    # For anything not caught by a more specific rule above, hand over to
    # the page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(crx_urls)),
    # Alternatively, if you want pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(crx_urls)),
]


# fmt: off
if settings.DEBUG:
    from django.conf.urls.static import static

    # Serve static and media files from development server
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # type: ignore
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # type: ignore
# fmt: on
