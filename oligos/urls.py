from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from oligos import views

router = DefaultRouter(schema_title='InjCalcAPI')
router.register(r'oligos', views.OligoViewSet)
router.register(r'accounts', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]