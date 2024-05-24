from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import WebSite
from .serializers import WebsiteSerializer, ScrapedWebSiteDetailSerializer

class ScrapedWebSiteListView(generics.ListAPIView):
    serializer_class = WebsiteSerializer
    permission_classes = [IsAuthenticated]    

    def get_queryset(self):
        return WebSite.objects.filter(user=self.request.user)
class ScrapedWebSiteDetailView(generics.RetrieveAPIView):
    serializer_class = ScrapedWebSiteDetailSerializer
    permission_classes = [IsAuthenticated]    
    lookup_field = 'id'

    def get_queryset(self):
        return WebSite.objects.filter(user=self.request.user)
