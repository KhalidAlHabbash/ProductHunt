from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == "GET":
        return render(request, 'accounts/signup.html')
    if request.POST["password1"] != request.POST["password2"]:
        return render(request, 'accounts/signup.html', {"error2": "Passwords do no match. Please try again."})
    else:
        try:
            if request.method == "POST":
                if request.POST["password1"] == request.POST["password2"]:
                    user = User.objects.get(username=request.POST["username"])
            return render(request, 'accounts/signup.html', {"error":"Username is registered to another account. Please try another one."})
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST["username"], password = request.POST["password1"])
        auth.login(request,user)
        return redirect ('home')

def nothing(request):
    return render(request,'accounts/login.html')

def login(request):
    if request.method=="GET":
        return render(request,'accounts/login.html')
    if request.method=="POST":
        user = auth.authenticate(username=request.POST["usernameL"],password=request.POST["passwordL"])
        if user is not None:
            auth.login(request,user)
            return redirect ('home')
        else:
            return render(request, 'accounts/login.html', {"errorL": "User is not registered. Username or password is incorrect"})
    else:
        return render(request, 'accounts/logout.html')




def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    else:
        return render(request,'accounts/logout.html')

def termsandprivacy(request):
    return render(request,'accounts/termsandprivacy.html')
