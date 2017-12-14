from django.conf.urls import url
from ajax import views
# Setup ajax endpoints here

urlpatterns = [
    url(r'^update/$', views.update_spells, name='update_spells')
]
