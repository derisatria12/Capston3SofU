from django.shortcuts import get_object_or_404, render

from menu.models import Category, Item
from vendor.models import Vendor

from django.db.models import Prefetch

# Create your views here.


def listtoko(request):
    vendors = Vendor.objects.filter(is_approved = True, user__is_active = True)
    vendor_count = vendors.count()

    
    context = {
        'vendors' : vendors,
        'vendor_count' : vendor_count,
    }
    return render(request, 'listtoko/listings.html', context)

def vendor_detail(request, vendor_slug):
    vendor = get_object_or_404(Vendor, vendor_slug = vendor_slug)

    categories = Category.objects.filter(vendor = vendor).prefetch_related(
        Prefetch(
            'item',
            queryset= Item.objects.filter(is_available = True)
        )
    )

    context = {
        'vendor' : vendor,
        'categories' : categories,
    }

    return render(request, 'listtoko/vendor_detail.html', context)