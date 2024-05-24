

from django.urls import path

from .views import ScrapedWebSiteDetailView, ScrapedWebSiteListView


urlpatterns = [
    
    path('', ScrapedWebSiteListView.as_view(), name='scraped-websites-list'),
    path('<int:id>/', ScrapedWebSiteDetailView.as_view(), name='scraped-website-details'),
]
