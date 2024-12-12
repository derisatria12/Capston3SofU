from django.contrib import admin

from menu.models import Category, Item

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'vendor', 'updated_at')
    search_fields = ('category_name', 'vendor__vendor_name')

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('item_title',)}
    list_display = ('item_title', 'category', 'vendor', 'price', 'is_available', 'updated_at')
    search_fields = ('item_title', 'category__category_name', 'vendor__vendor_name', 'price')
    list_filter = ('is_available', )

# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
