from django.conf.urls import url
#from . import views
from my_post import views

app_name = 'my_post'

urlpatterns = [
    url(r'^$', views.article_list, name='register'),
]
