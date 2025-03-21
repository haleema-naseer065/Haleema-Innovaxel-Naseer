from django.db import models

class ShortURL(models.Model):
    url = models.URLField()
    shortCode = models.CharField(max_length=15, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.shortCode
