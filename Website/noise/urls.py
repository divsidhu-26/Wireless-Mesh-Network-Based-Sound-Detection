from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^sensors/(?P<pk>[0-9]+)/$',views.SensorDetail.as_view()),
    url(r'^sensors/$',views.SensorList.as_view()),
    url(r'^list_sensors/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^list_sensors/$',views.index,name='index'),

]

urlpatterns = format_suffix_patterns(urlpatterns)