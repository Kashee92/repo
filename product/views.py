from django.shortcuts import render, redirect
from . models import Prod_Cat, Product
from django.contrib import messages
import datetime
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator

# Home Page
def home(request):
    #Adding the Ad Post 
    if request.method == 'POST':
        user = request.user
        now = datetime.datetime.now()
        user_id = User.objects.get(id=user.id)
        category = request.POST.get('prodcat')
        title = request.POST.get('prodtitle')
        desc = request.POST.get('proddesc')
        condition = request.POST.get('prodcondition')
        price = request.POST.get('prodprice')
        location = request.POST.get('prodlocation')
        phone = request.POST.get('phone')
        pic1 = request.FILES['pic1']
        pic2 = request.FILES['pic2']
        pic3 = request.FILES['pic3']
        pic4 = request.FILES['pic4']

        product = Product(user=user_id, user_phone= phone, prod_cat=category, prod_title=title, prod_desc=desc, prod_condition=condition, prod_price=price, prod_location=location, prod_date=now , image1=pic1, image2=pic2, image3=pic3, image4=pic4)
        product.save()
       
        messages.success(request,'Your AD has been posted successfully')
        return redirect('/')

    categories = Prod_Cat.objects.all()
    product = Product.objects.all()
    n = len(product)
    return render(request, 'home.html', {'categories' : categories, 'products':product, 'no_of_prods' : n})

# Ad Post
def post_ad(request):
    if request.user.is_authenticated:
        categories = Prod_Cat.objects.all()
        return render(request, 'adpost.html', {'categories' : categories})

    if request.method == 'POST':
        title = request.POST.get('prodtitle')
        return render(request, 'home.html')

    else:
        messages.error(request,'Please Login to Post a AD')
        return render(request, 'login.html')

# All Ads Pge
def AllClassifieds(request, id):
        context = {}
        cat_count = []
        prod_list = Prod_Cat.objects.all()
        for plist in prod_list:
            prod = Product.objects.filter(prod_cat = plist.cat_name).count()
            #print(prod)
            cat_count.append(prod)

        context['prod_list'] = prod_list
        context['cat_count'] = cat_count
        cat = Prod_Cat.objects.get(cat_id = id)
        name = cat.cat_name
        products = Product.objects.filter(prod_cat = name).order_by('prod_id')
        
        #Pagination
        paginator = Paginator(products, 3) # Show 3 products per page.
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)

        context['products'] = products
        if not products:
            messages.error(request,'No items in this category')
            return redirect('/')
        else:
            return render(request, 'AllClassifieds.html', context)
        
# Product Detail        
def ProductDetail(request, id):
        products = Product.objects.get(prod_id = id)
        print(products.prod_desc)
        if products is not None:
            return render(request, 'ProductDetail.html', {'products':products})
        else:
            return render(request, 'home.html')

# Search a Product
def search_item(request):
    item = request.GET.get('item')
    products = Product.objects.filter(Q(prod_title__contains=item) | Q(prod_desc__contains=item))
    print(products)
    return render(request, 'AllClassifieds.html', {'products':products})

