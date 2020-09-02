from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

@login_required
def upvote(request,product_id):
    if request.method == "POST":
        products = get_object_or_404(Product, pk=product_id)
        products.product_votes += 1
        products.save()
        return redirect('/products/' + str(products.id))



def home(request):
    all_products = Product.objects
    return render(request,'product/home.html', {"all_products":all_products})

def detail(request,product_id):
    products = get_object_or_404(Product,pk=product_id)
    return render(request,'product/detail.html', {'products':products})

@login_required
def create(request):
    if request.method == "POST":
        if request.POST["product-title"] and request.POST["product-desc"] and request.POST["URL"] and request.FILES["product-icon"] and request.FILES["product-image"]:
            product = Product()
            product.product_title = request.POST["product-title"]
            product.product_desc = request.POST["product-desc"]
            product.product_icon = request.FILES["product-icon"]
            product.product_image = request.FILES["product-image"]
            product.product_date = timezone.datetime.now()
            product.hunter = request.user
            if request.POST["URL"].startswith ("https://") or request.POST["URL"].startswith("http://"):
                product.product_url = request.POST["URL"]
            else:
                product.product_url = "http://" + request.POST["URL"]

            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'product/create.html', {"errorP":"Please fill in all the fields"})
    else:
        return render(request, 'product/create.html')




