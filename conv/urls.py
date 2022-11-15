from django.contrib import admin
from django.urls import path
# Views
from con.views import index1

urlpatterns = [
    path('admin/', admin.site.urls),
    # Index
    path('', index1, name='index1')
]