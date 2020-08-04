from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def home(request):
    return render(request,'product/home.html')

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
            return redirect('home')
        else:
            return render(request, 'product/create.html', {"errorP":"Please fill in all the information required"})
    else:
        return render(request, 'product/create.html')




