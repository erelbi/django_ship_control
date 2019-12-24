from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf.urls import url
from .models import Ship
from . import models



urlpatterns = [
    path("", views.IndexView.as_view(), name='home'),
 
    url(r'^ships/(?P<pk>\d+)/$', views.ship_lastports, name='ship_lastport'),
    url(r'^signup/$', views.signup, name='signup'),
   # url(r'^ships/(?P<pk>\d+)/new/$', views.cargo, name='cargo'),
    url(r'^infoedit/$', views.shipinformation, name='info'),
    url(r'^addengine/$', views.add_engineer, name='engine'),

  #  url(r'^ships/(?P<pk>\d+)/$', views.ship_lastport, name='ship_lastport'),
    url(r'^postinfo/$', views.info_get, name='post'),
    path('thankyou/', views.info_get),
    path('ships/<int:pk>/edit/', views.info_edit, name='info_edit'),
]