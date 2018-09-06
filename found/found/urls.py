from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('my_post.urls')),
    url(r'^about/$',views.about),
    url(r'^$',views.homepage),
]