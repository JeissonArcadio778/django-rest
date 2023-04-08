from projects.models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer


# Who will access to the data/functions in Django. Authentication. 
class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Project.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = ProjectSerializer