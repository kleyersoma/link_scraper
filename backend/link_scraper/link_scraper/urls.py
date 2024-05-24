"""
URL configuration for link_scraper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from authentication.views import RegisterView, LoginView
from websites.views import ScrapedWebSiteListView, ScrapedWebSiteDetailView
from website_scraper.views import ScrapeURLView

from django.urls import path, include

from django.contrib import admin, sites

urlpatterns = [
    # Authentication API
    path('api/', include('authentication.urls')),
    # Website Scraper API
    path('api/website-scraper/', include('website_scraper.urls')),
    # Websites Scraped API
    path('api/scraped-websites/', include('websites.urls')),
]
