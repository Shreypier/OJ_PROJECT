from django.urls import path
from django.contrib import admin
from Online_Compiler.views import problem_page# Import views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Online_Compiler.views import problem
from django.conf.urls.static import static

urlpatterns = [
    path('',problem_page,name='result'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
