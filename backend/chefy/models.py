from django.db import models
from django.db.models import JSONField
# Create your models here.


class ChefyRecipeModel(models.Model):
    chat_gpt_response = models.CharField(max_length=5000)
    user = models.CharField(max_length=256)
    

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Chefy Recipe Gen"
        verbose_name_plural = "Chefy Model"
        db_table = "chefy_recipe"

