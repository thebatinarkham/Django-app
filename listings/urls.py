from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('listing/create', views.CreateListings.as_view(), name='create'),
    path('listing/update/<int:pk>', views.ListingUpdate.as_view(), name='update'),
    path('listing/delete/<int:pk>', views.DeleteListing.as_view(), name='delete'),
    
] 


