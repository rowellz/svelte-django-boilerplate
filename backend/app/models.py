from django.db import models
from django.db.models import JSONField


class DjangoAppModel(models.Model):
    entry = models.CharField(max_length=5000)
    user = models.CharField(max_length=256)
    

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Django App Model"
        verbose_name_plural = "Django App Model"
        db_table = "django_app_model"

