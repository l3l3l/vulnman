from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from apps.projects.models import Project


class VulnmanModel(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

    @staticmethod
    def has_read_permission(request):
        return True

    @staticmethod
    def has_write_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    def has_object_write_permission(self, request):
        return True


class VulnmanProjectModel(VulnmanModel):
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    command_created = models.ForeignKey('commands.CommandHistoryItem', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

    @staticmethod
    def has_create_permission(request):
        project = request.data.get('project')
        if project and Project.objects.filter(pk=project, creator=request.user).exists():
            return True
        return False

    @staticmethod
    def has_read_permission(request):
        return True

    @staticmethod
    def has_update_permission(request):
        return True

    @staticmethod
    def has_destroy_permission(request):
        return True

    def has_object_write_permission(self, request):
        return request.user == self.project.creator

    def has_object_update_permission(self, request):
        project = request.data.get('project')
        if project and Project.objects.filter(pk=project, creator=request.user).exists():
            return True
        elif project is None:
            return self.project.creator == request.user
        return False
