from django.shortcuts import render
from django.shortcuts import HttpResponse
 
#import Models
from .models import Product
from .models import Category 
#def home(request):
    #myText = "My Response"
    #context = {'templateNameForMyText': myText}
#    return render( request, 'ProductCatalogApp/Home.html', context)
 

def product_list(request, category_slug=None):
    """
    Lista los productos visibles de una categoria.
    Si no se indica categoria, lista todos los productos visibles.
    """
    category = None
    categories = Category.objects.all() #Todas las categorias
    products = Product.objects.filter(visibility=True)  #Lista los productos que se pueden mostrar (visibility=True)
    if category_slug: #Si existe un category_slug (o sea, es distinto de None)
        category = get_object_or_404(Category, slug=category_slug)  #obtiene la categoria desde la DB, sino existe la categoria manda 404.
        products = products.filter(category=category)   #filtra los productos dejando los de la categoria
    #return render(request, 'ProductCatalogApp/product/list.html',{'category': category, 'categories': categories, 'products': products})
    return render(request, 'ProductCatalogApp/list.html',{'category': category, 'categories': categories, 'products': products})



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, visibility=True)
    cart_product_form = CartAddProductForm()
    #return render(request, 'ProductCatalogApp/product/detail.html',{'product': product, 'cart_product_form': cart_product_form})
    return render(request, 'ProductCatalogApp/detail.html',{'product': product, 'cart_product_form': cart_product_form})