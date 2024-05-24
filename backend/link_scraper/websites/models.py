from django.db import models
from django.contrib.auth.models import User

class WebSite(models.Model):
    user = models.ForeignKey(User, related_name='scraped_websites', on_delete=models.CASCADE)
    url = models.URLField()
    website_name = models.CharField(max_length=255)
    scraped = models.BooleanField(default=False)
    link_count = models.IntegerField(default=0)

    def __str__(self):
        return self.website_name
    
    class Meta:
        unique_together = ('user', 'url') # Ensure the combination of user and url is unique

class Link(models.Model):
    website = models.ForeignKey(WebSite, related_name='links', on_delete=models.CASCADE)
    url = models.URLField()
    name = models.TextField()

    def __str__(self):
        return self.url

