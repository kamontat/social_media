from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.CharField("Description", max_length=150)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
