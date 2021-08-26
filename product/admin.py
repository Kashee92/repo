from django.contrib import admin
from . models import Product, Prod_Cat

# Register your models here.
#admin.site.register(Product)
#admin.site.register(Prod_Cat)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'prod_id', 'prod_cat', 'prod_title', 'prod_desc', 'user_phone', 'prod_condition', 'prod_price', 'prod_location', 'prod_date']

@admin.register(Prod_Cat)
class Prod_catAdmin(admin.ModelAdmin):
    list_display = ['cat_id', 'cat_name', 'cat_slug']