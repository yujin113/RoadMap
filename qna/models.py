from django.db import models
from django.utils import timezone

# Create your models here.
class Qna(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default = timezone.now)
    body = models.TextField()

    def __str__(self) :
        return self.title

    def summary(self) :
        return self.body[:100]