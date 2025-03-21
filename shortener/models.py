from django.db import models

# Create your models here.
class ShortURL(models.Model):
    url = models.URLField()
    short_code = models.CharField(max_length=15, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.PositiveIntegerField(default=0)

def __str__(self):
        return self.short_code
