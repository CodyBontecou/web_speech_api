from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from algorithm.views import next_practice_item

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('item/next/', next_practice_item, name='next-song')
]
