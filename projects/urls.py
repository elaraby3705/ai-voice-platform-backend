from django.urls import path 
from .views import ProjectListCreateView, ProjectDetailView

urlpatterns = [
    path("", ProjectDetailView.as_view(), name= "project-list"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
]