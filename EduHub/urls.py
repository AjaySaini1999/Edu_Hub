from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "Education Hub"
admin.site.index_title = "Welcome to Education Hub"
admin.site.site_title = "Education Hub"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hub.urls'))
]
