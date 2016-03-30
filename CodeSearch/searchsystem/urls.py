from django.conf.urls import url

from . import views

app_name = 'searchsystem'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index\.html$', views.index, name='index'),
    url(r'^result/$', views.search, name='search'),
    url(r'^result/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
]
