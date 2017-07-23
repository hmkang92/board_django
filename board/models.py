# board/models.py
from django.db import models

class Post(models.Model):
    detection_at = models.DateTimeField()
    title = models.CharField(max_length=100, verbose_name='title', help_text='')
    spread_ip = models.GenericIPAddressField()
    waypoint_ip = models.GenericIPAddressField()
    spread_route = models.TextField()
    spread_feature_text = models.TextField()
    spread_feature_image = models.ImageField(blank=True)
    detection_pattern = models.TextField()
    #report_file = models.FileField()
    author = models.CharField(max_length=20)
    tag_set = models.ManyToManyField('Tag') # blank=True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name