from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin
from links import views


admin.autodiscover()

router = routers.SimpleRouter()
router.register(r'links', views.LinkViewSet)


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^r/', views.redirectView)
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()


