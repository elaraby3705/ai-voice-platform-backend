from django.db import models
from django.conf import settings
from projects.models import project
# Create your models here.

class VoiceSession(models.Model):
    project =models.ForeignKey(
        Project,
        on_delete = models.CASCADE,
        related_name= "sessions"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name = "sessions"
    )
    session_id  = models.CharField(max_length=255, unique = True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    duration_seconds =models.IntegerField(null=True, blank=True)

    # extra metadata (optional)
    final_transcript = models.TextField(null=True, blank=True)
    audio_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"session {self.session_id} for project {self.project.id}"