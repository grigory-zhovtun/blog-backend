from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import os

from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))
    # или
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
