from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from my_post import views as my_post_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^my_post/', include('my_post.urls')),
    url(r'^about/$',views.about),
    url(r'^$',my_post_views.article_list),
]

urlpatterns += staticfiles_urlpatterns()