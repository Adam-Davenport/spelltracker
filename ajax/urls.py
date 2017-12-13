from django.conf.urls import url
from ajax import views
# Setup ajax endpoints here

urlpatterns = [
    url(r'^udpate/$', views.update_tracker, name='ajax_update')
]
