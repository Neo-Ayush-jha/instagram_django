from django.contrib import admin
from django.urls import path
from School.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("home/",accountHome),
    path("account/<int:id>/",insta,name="singlePost"),
    path("/delete/<int:id>/",deleteStudent,name="delete"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

