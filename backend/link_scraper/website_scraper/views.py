from rest_framework import generics, status, serializers
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from websites.models import WebSite
from websites.serializers import ScrapedWebSiteDetailSerializer

from .serializers import ScrapURLSerializer

import logging

logger = logging.getLogger(__name__)

class ScrapeURLView(generics.CreateAPIView):
    serializer_class = ScrapURLSerializer
    permission_classes = [IsAuthenticated]

    
    def post(self, request:Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                url = serializer.validated_data.get('url')
                user_id = request.user.id
                scraped_page = serializer.save()
                detail_serializer = ScrapedWebSiteDetailSerializer(scraped_page)
                return Response(detail_serializer.data, status=status.HTTP_201_CREATED)
            except serializers.ValidationError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
