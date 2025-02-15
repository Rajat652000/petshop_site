from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from home.models import contact
# Create your views here.
#Timesys@123
def index(request):
    if request.user.is_anonymous:
        return redirect(userlogin)
    pets = [
        {"name": "afghan Hhound", "image": "images/afghan_hound.jpg", "description": "A cute white kitten."},
        {"name": "Airedale Terrier", "image": "images/Airedale_Terrier.jpg", "description": "A friendly golden retriever."},
        {"name": "Akita", "image": "images/Akita.jpg", "description": "A playful beagle."},
        {"name": "Alaskan Husky", "image": "images/Alaskan_husky.jpg", "description": "A playful beagle."},
        {"name": "Alaskan Malamute", "image": "images/Alaskan_malamute.jpg", "description": "A playful beagle."},
        {"name": "American Bulldog", "image": "images/American_bulldog.jpg", "description": "A playful beagle."},
        {"name": "American Eskimo", "image": "images/American_eskimo.jpg", "description": "A playful beagle."},
        {"name": "American Terrier", "image": "images/American_staffordshire_terrier.jpg", "description": "A playful beagle."},
        {"name": "American Foxhund", "image": "images/American_foxhund.jpg", "description": "A playful beagle."},
        {"name": "Australian Bulldog", "image": "images/Australian_bulldog.jpg", "description": "A playful beagle."},
        {"name": "Australian Cattle", "image": "images/Australian_cattle.jpg", "description": "A playful beagle."},
    ]
    return render(request,'index.html',{"pets":pets})

def userlogin(request):
    if request.method=="POST":
        name = request.POST.get("name")
        password = request.POST.get("password")

        user = authenticate(username=name, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request, 'login.html') 
    return render(request, 'login.html')

def userlogout(request):
    logout(request)
    return redirect(userlogin)

def About(request):
    if request.user.is_anonymous:
        return redirect(userlogin)
    return render(request,"about.html")
 
def Contact(request):
    if request.user.is_anonymous:
        return redirect(userlogin)
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        city = request.POST.get('city')
        porpose = request.POST.get('porpose')
        Contact = contact(name=name, phone=phone, email=email, city=city, porpose=porpose)
        Contact.save()
    return render(request,"contact.html")

def Product(request):
    if request.user.is_anonymous:
        return redirect(userlogin)
    products = [
        {"name": "DOG FOOD", "image": "images/pet1.webp", "description":"","price": "2."},
        {"name": "CAT FOOD", "image": "images/pet2.webp", "description": "","price": "2."},
        {"name": "TREATS", "image": "images/pet3.webp", "description": "","price": "3."},
        {"name": "PREMIUM FOOD", "image": "images/pet4.webp", "description": "","price": "5."},
        {"name": "PRESCRIPTION DIET", "image": "images/pet5.webp", "description": "","price": "10."},
        {"name": "TOYS", "image": "images/pet6.webp", "description": "","price": "6."},
        {"name": "PHARMACY", "image": "images/et7.webp", "description": "","price": "9."},
        {"name": "CLOTHING", "image": "images/pet8.png", "description": "","price": "12."},
        {"name": "LITTER SUPPLIES", "image": "images/pet9.webp", "description": "","price": "12."},
        {"name": "GROOMING", "image": "images/pet10.webp", "description": "","price": "3."},
        {"name": "BEDS AND METS", "image": "images/pet11.png", "description": "","price": "30."},
    ]
    return render(request,"product.html",{"products":products})