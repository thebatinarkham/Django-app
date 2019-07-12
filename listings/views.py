from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Listing


def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
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

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  
  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)
  
class CreateListings(CreateView):
        model = Listing
        template_name = "listings/create.html"
        fields = [ 'realtor', 'title', 'address','state','city','zipcode','zipcode','price','bedrooms','bathrooms','sqft','lot_size','description'
        ,'photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6','is_publised','list_date']
        success_url = '/'

class ListingUpdate(UpdateView):
    model = Listing
    template_name = 'listings/update.html'
    fields = [ 'realtor', 'title', 'address','state','city','zipcode','zipcode','price','bedrooms','bathrooms','sqft','lot_size','description'
        ,'photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6','is_publised','list_date']

    def form_valid(self, form):
        instance = form.save()
        return redirect( '/')

class DeleteListing(DeleteView):
        model = Listing
        template_name = "listings/delete.html"
        success_url = '/'



