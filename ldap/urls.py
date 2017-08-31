from django.conf.urls import url
from ldap import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^ldap/$', views.SearchLdap.as_view()),

    ]

urlpatterns = format_suffix_patterns(urlpatterns)
