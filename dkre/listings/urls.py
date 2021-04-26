from django.urls import path

from . import views

# pertains to /listings
# for a single listing: /listings/23
# needs a parameter in URL
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]