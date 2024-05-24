
from django.urls import path
from .views import ScrapeURLView


urlpatterns = [
    path('scrape-website/', ScrapeURLView.as_view(), name='scrape-website')
]

    