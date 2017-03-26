from django.conf.urls import url

from . import views

app_name = 'Audio_Archive'
urlpatterns = [
    url(r'^$', views.program, name='program'),
    url(r'^(?P<talk_id>[0-9]+)/$', views.talk, name='talk_detail')
]