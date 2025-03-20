from django.db import models

# Create your models here.
class ShortenedURL(models.Model):
  original_url = models.URLField()
  shorten_code = models.CharField(max_length = 10,unique = True)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  access_count = models.IntegerField(default = 0)

  def __str__(self):
    return f"{self.orignal_url}->{self.shorten_code}(Accessed {self.access_count} times)"