from django.db import models
import uuid
from django.template.defaultfilters import slugify

# Create your models here.
class Source(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200, unique=True, blank=True)
  url = models.URLField()

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    super(Source, self).save(*args, **kwargs)

  def __str__(self):
    return self.name

class Article(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=200)
  description = models.TextField()
  content = models.TextField()
  url = models.URLField()
  image = models.URLField()
  publishedAt = models.DateTimeField()
  source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='articles', null=True, blank=True)

  def __str__(self):
    return self.title
  
