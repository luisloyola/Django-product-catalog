from django.contrib import admin
from .models import Category
from .models import Product
#from .models import ProductDetail

# Register your models here.
#admin.site.register(Category)
#admin.site.register(Product)
#admin.site.register(ProductDetail)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'brand', 'model', 'price', 'stock', 'visibility', 'created', 'updated']
    list_filter = ['visibility', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'visibility']
    prepopulated_fields = {'slug' : ('name',)}
admin.site.register(Product,ProductAdmin)

#class ProductDetailAdmin(admin.ModelAdmin):
#    list_display = ...