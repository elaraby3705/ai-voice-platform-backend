# Projects/ serializers.py 
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class meta: 
        model = Project
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
        