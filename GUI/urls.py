from django.conf.urls import url, include
from GUI.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]