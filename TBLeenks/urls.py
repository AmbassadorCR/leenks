from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin
from links import views


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'links', views.LinkViewSet)


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
