from rest_framework import serializers
from .models import WebSite, Link

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebSite
        fields = ['id', 'url', 'website_name', 'link_count', 'scraped']


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        
        fields = ['id', 'website', 'url', 'name']


class ScrapedWebSiteDetailSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = WebSite
        fields = ['id', 'url', 'website_name', 'link_count', 'links']
