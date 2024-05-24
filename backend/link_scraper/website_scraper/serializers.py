from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from websites.models import WebSite, Link
from .scraper import scrape_website


class ScrapURLSerializer(serializers.Serializer):
    url = serializers.URLField()


    def create(self, validated_data):
        url = validated_data.get('url')
        request = self.context.get('request')
        user = request.user

        if not isinstance(user, get_user_model()):
            raise ValueError('User must be authenticated.')
        
        title, links = scrape_website(url)

        # Add/Save WebSite as scraped
        try:
            scraped_website, created = WebSite.objects.update_or_create(
                user=user, 
                url=url, 
                defaults={
                    'website_name': title, 
                    'link_count': len(links),
                },
                scraped=True)
            
            # if the website was not newly created, clear the old links
            if not created:
                scraped_website.links.all().delete()
            
            # Save Links 
            for link in links:
                Link.objects.create(website=scraped_website,url=link.get('url'), name=link.get('name'))

            return scraped_website
        except IntegrityError as e:
            raise serializers.ValidationError('An error occured while saving the scraped data.')
