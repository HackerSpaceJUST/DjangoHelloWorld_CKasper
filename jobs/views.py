from django.shortcuts import redirect
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions

from .models import Job
from .serializers import JobSerializer, UserSerializer

class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows jobs to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

def apply(request, job_id):
    if request.user.is_authenticated:
        job = Job.objects.get(pk=job_id)
        job.applicands.add(request.user)

    return redirect('/jobs/{job_id}'.format(job_id=job_id))