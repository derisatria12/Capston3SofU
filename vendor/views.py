
from django.shortcuts import render, get_object_or_404, redirect

from menu.forms import CategoryForm, ItemForm


from .forms import VendorForm
from accounts.forms import UserProfileForm

from accounts.models import UserProfile
from .models import Vendor
from django.contrib import messages

from menu.models import Category, Item
from django.template.defaultfilters import slugify


def get_vendor(request):
    vendor = Vendor.objects.get(user=request.user)
    return vendor

def vprofile(request):
    profile = get_object_or_404(UserProfile, user = request.user)
    vendor = get_object_or_404(Vendor, user = request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        vendor_form = VendorForm(request.POST, request.FILES, instance=vendor)
        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request, 'Settings updated')
            return redirect('vprofile')
        else:
            print(profile_form.errors)
            print(vendor_form.errors)
    else:
        profile_form = UserProfileForm(instance= profile)
        vendor_form = VendorForm(instance= vendor)

    context = {
        'profile_form': profile_form,
        'vendor_form': vendor_form,
        'profile' : profile,
        'vendor' : vendor,
    }

    return render(request, 'vendor/vprofile.html', context)

def menu_builder(request):
    vendor = get_vendor(request)
    categories = Category.objects.filter(vendor=vendor).order_by('created_at')
    context = {
        'categories' : categories,
    }

    return render(request, 'vendor/menu_builder.html', context)

def item_by_category(request, pk=None):
    vendor = get_vendor(request)
    category = get_object_or_404(Category, pk = pk)
    item = Item.objects.filter(vendor = vendor, category=category)
    context = {
        'item' : item,
        'category' : category,
    }
    return render(request, 'vendor/item_by_category.html', context)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.vendor = get_vendor(request)
            category.slug = slugify(category_name)
            form.save()
            messages.success(request, 'Category added successfully')
            return redirect('menu_builder')
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    context = {
        'form' : form,

    }
    return render(request, 'vendor/add_category.html', context)

def edit_category(request, pk=None):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.vendor = get_vendor(request)
            category.slug = slugify(category_name)
            form.save()
            messages.success(request, 'Category Updated successfully')
            return redirect('menu_builder')
        else:
            print(form.errors)
    else:
        form = CategoryForm(instance=category)
    context = {
        'form' : form,
        'category' : category, 

    }
    return render(request, 'vendor/edit_category.html', context)

def delete_category(request, pk = None):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, 'Category has been Deleted successfully')
    return redirect('menu_builder') 

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            itemtitle = form.cleaned_data['item_title']
            item = form.save(commit=False)
            item.vendor = get_vendor(request)
            item.slug = slugify(itemtitle)
            form.save()
            messages.success(request, 'Item added successfully')
            return redirect('item_by_category', item.category.id)
        else:
            print(form.errors)
    else:
        form = ItemForm()
        #modify form
        form.fields['category'].queryset = Category.objects.filter(vendor = get_vendor(request))
    context = {
        'form' : form,

    }
    return render(request, 'vendor/add_item.html', context)

def edit_item(request, pk=None):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            itemtitle = form.cleaned_data['item_title']
            item = form.save(commit=False)
            item.vendor = get_vendor(request)
            item.slug = slugify(itemtitle)
            form.save()
            messages.success(request, 'Item Updated successfully')
            return redirect('item_by_category', item.category.id)
        else:
            print(form.errors)
    else:
        form = ItemForm(instance=item)
        form.fields['category'].queryset = Category.objects.filter(vendor = get_vendor(request))
    context = {
        'form' : form,
        'item' : item, 

    }
    return render(request, 'vendor/edit_item.html', context)

def delete_item(request, pk = None):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    messages.success(request, 'Item has been Deleted successfully')
    return redirect('item_by_category', item.category.id) 