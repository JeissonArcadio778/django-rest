from rest_framework import serializers
from .models import Project

# Djagngo will know what information send to the client. 
class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = '__all__'
    read_only_fields = ('created_at',)