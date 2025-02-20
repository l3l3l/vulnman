from django.db import models
from vulnman.models import VulnmanProjectModel
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class Employee(VulnmanProjectModel):
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    position = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = [("project", "email")]
        ordering = ["-date_updated"]

    def __str__(self):
        if self.first_name and self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        elif self.last_name:
            return self.last_name
        return self.email

    def get_absolute_url(self):
        return reverse_lazy('projects:social:employee-detail', kwargs={'pk': self.pk})


class Credential(VulnmanProjectModel):
    username = models.CharField(max_length=256)
    cleartext_password = models.CharField(max_length=255, blank=True, null=True)
    hashed_password = models.CharField(max_length=512, blank=True, null=True)
    location_found = models.CharField(max_length=512)
    valid_services = models.ManyToManyField('networking.Service', blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Credentials"
        verbose_name = "Credential"
        ordering = ["-date_updated"]

    def get_valid_services(self):
        values = []
        for service in self.valid_services.all():
            values.append("%s (%s)" % (service.host, service))
        return values

    def get_absolute_update_url(self):
        return reverse_lazy('projects:social:credential-update', kwargs={'pk': self.pk})

    #def get_absolute_delete_url(self):
    #    return reverse_lazy('projects:social')