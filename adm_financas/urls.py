from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from cliente import urls as cliente_urls

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('cliente/', include(cliente_urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


"""
from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from cliente import urls as cliente_urls

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', include(home_urls)),
	path('cliente/', include(cliente_urls)),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    
  
]
"""
