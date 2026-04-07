
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class EmailScan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email_text = models.TextField()
    prediction = models.CharField(max_length=20)
    confidence = models.FloatField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)