from django.conf.urls import url
from .import views


app_name= 'dashboard'

urlpatterns = [
    url(r'^$', views.dashboard_detail, name="dashPage"),
    # http://localhost:8000/dashboard/profile/
    url(r'^profile/$', views.profile_detail, name="profilePage"),
    url(r'^profile/(?P<pk>\d+)/$', views.profile_detail, name="profilePage_with_pk"),
    url(r'^awards/$', views.awards_detail, name="awardsPage"),
    url(r'^myAccountabilityPartners/$', views.myAccountabilityPartners_detail, name="mapPage"),
    url(r'^findAccountabilityPartners/$', views.findAccountabilityPartners_detail, name='fapPage'),
    # http://localhost:8000/dashboard/healthData/
    url(r'^healthData/$', views.health_view, name='health'),
    url(r'^healthData/edit$', views.editHealth_view, name='edit_health'),
    # http://localhost:8000/dashboard/genralData/
    url(r'^generalData/$', views.general_view, name='general'),
    # lose and add friends
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='changeFriend')
]
