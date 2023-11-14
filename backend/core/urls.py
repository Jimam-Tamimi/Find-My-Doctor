from django.urls import path, include, re_path
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('api/account/', include("account.urls")), 
    path('api/', include("hospital.urls")),  
    
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
