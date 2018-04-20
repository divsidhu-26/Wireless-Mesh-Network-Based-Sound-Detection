"""Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from noise import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^noise/', include('noise.urls')),
    url(r'^sensors/(?P<pk>[0-9]+)/$',views.SensorDetail.as_view()),
    url(r'^sensors/$',views.SensorList.as_view()),
    url(r'^map_sensors/$',views.detail,name='detail'),
    url(r'^list_sensors/$',views.index,name='index'),
    url(r'^$',views.home,name='home'),
    url(r'^future/$',views.future),
    url(r'^team/$',views.team),
    url(r'^ajax/get_context/$', views.get_context, name='get_context'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
