from django.conf.urls import patterns, include, url

from .views import HomeListView

urlpatterns = patterns('',

    url(r'^$' , HomeListView.as_view(), name='home'),

)