from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/custom/$', views.snippet_custom),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail)
    ]
