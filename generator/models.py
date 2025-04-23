from django.db import models
from users.models import User

# Create your models here.



class PromptHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompted_at = models.DateField(auto_now_add=True)
    topic = models.CharField(null=False)
    reponses = models.TextField()