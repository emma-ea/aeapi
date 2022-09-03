from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'img', views.APViewSet)

urlpatterns = [
        path('about/', views.index, name='index'),
        path('v1/', include(router.urls)),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
