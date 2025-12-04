# serializers.py
from rest_framework import  serializers
from .models import VoiceSession
from projects.models import Project

class VoiceSessionSerializer(serializers.ModelSerializer):
    project = serializers.CharField(source="project.title", read_only=True)
    
    class Meta:
        model = VoiceSession
        fields = [
            "id", 
            "project",
            "started_at",
            "duration_seconds",
            "created_by",
        ]
        read_only_fields = ["id", "project","created_at", "duration_seconds"]
        
class VoiceSessionCreateSerializer(serializers.ModelSerializer):
    model = VoiceSession
    fields = ["id"]
    
    def create (self, validated_data):
        project = self.context["project"]
        user = self.context["request"].user
        return  VoiceSession.objects.create(project=project, created_by=user)
    