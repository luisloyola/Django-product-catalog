#from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse


@python_2_unicode_compatible  # only if you need to support Python 2
class Category(models.Model):
    name = models.CharField(max_length=200, db_index = True)
    slug = models.SlugField(max_length=200, db_index = True, unique = True)
    #url friendly ID
    
    class Meta:
    	ordering = ('name',)
    	verbose_name = 'category'
    	verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
    	return reverse('ProductCatalogApp:product_list_by_category', args=[self.slug])



 
@python_2_unicode_compatible  # only if you need to support Python 2
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    visibility = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    #myDate = models.DateTimeField('date published')

    class Meta:
        ordering =('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
    	return reverse('ProductCatalogApp:product_detail', args=[self.id, self.slug])

#@python_2_unicode_compatible  # only if you need to support Python 2
#class ProductDetail(models.Model):
#    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
#    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
#    description = models.TextField(blank=True)

#    #myDate = models.DateTimeField('date published')
    
#    def __str__(self):
#        return self.Product.mame() + '\'s details'
#    def __unicode__(self):
#        return u"%s" % self.Product.name + '\'s details'

