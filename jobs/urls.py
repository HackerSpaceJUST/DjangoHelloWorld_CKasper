from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'jobs', views.JobViewSet)
router.register(r'users', views.UserViewSet)

app_name = 'jobs'
urlpatterns = [
    path('', include(router.urls)),
    path('jobs/<int:job_id>/apply', views.apply, name='apply'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]