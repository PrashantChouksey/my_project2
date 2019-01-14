from django.shortcuts import  get_object_or_404,render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import state_choices,price_choices,bedroom_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)
    paginator = Paginator(listings,  6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    context={
        'listings':paged_listing,

    }

    return render(request, 'listing/listing.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listings':listing
    }
    return render(request, 'listing/listings.html', context)

def search(request):
    query_set_list = Listing.objects.order_by("-list_date")
    # Keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set_list = query_set_list.filter(description__icontains=keywords)
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set_list = query_set_list.filter(city__iexact=city) # City
    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_set_list = query_set_list.filter(state__iexact=state)
    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_set_list = query_set_list.filter(badrooms__lte=bedrooms)
    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_set_list = query_set_list.filter(price__lte=price)

    context = {
        'state_choices':state_choices,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'listings':query_set_list,
        'values':request.GET,
    }
    return render(request, 'listing/search.html', context)