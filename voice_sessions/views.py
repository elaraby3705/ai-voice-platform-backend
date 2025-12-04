from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import  get_object_or404
# Create your views here.

from .models import VoiceSession
from .serializers import  (
    VoiceSessionSerializer,
    VoiceSessionCreateSerializer,
)
from projects.models import Project
from .permissions import IsProjectOwner

class VoiceSessionListView(generics.ListAPIView):
    serializer_class = VoiceSessionSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return  VoiceSession.objects.filter(created_by=self.request.user)

class StartSessionAPIView(generics, CreateAPIView):
    serializer_class = VoiceSessionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, project_id):
        project = get_object_or_404(Project, id=project_id)

        # validate project ownership
        if project.owner!= request.user:
            return Response(
                {"details": "You do not own this project . "},
                status= status.HTTP_403_FORBIDDEN,
            )
        serializer = self.get_serializer(
            data = {}, context= {"project": project, "request":request}
        )
        serializer.is_valid(raise_on_error=True)
        session = serializer.save()

        return Response(
            VoiceSessionSerializer(session).data,
            status=status.HTTP_201_CREATED,
        )
class FinishSessionAPIView(generics.UpdateAPIView):
    serializer_class = VoiceSessionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, session_id):
        session = get_object_or_404(
            VoiceSession, id=session_id, created_by=request.user
        )

        if session.ended_at:
            return Response(
                {"detail": "Session already finished."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        session.finish()
        return Response(VoiceSessionSerializer(session).data)