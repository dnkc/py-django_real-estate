from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import price_choices, bedroom_choices, state_choices

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) #fetches listings from the database

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,

    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords and len(keywords) > 0:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    # city filter
    if 'city' in request.GET:
        city = request.GET['city']
        if city and len(city) > 0:
            queryset_list = queryset_list.filter(city__iexact=city) # iexact is case INsensitive
    # province
    if 'province' in request.GET:
        province = request.GET['province']
        if province and len(province) > 0:
            queryset_list = queryset_list.filter(province__iexact=province)
    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms and len(bedrooms) > 0:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms).order_by('-bedrooms')
    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price and len(price) > 0:
            queryset_list = queryset_list.filter(price__lte=price).order_by('-price')

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)