from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'page1.html',{})

class Accueil(View):
    def get(self,request):
        return render(request,'page1.html',{})

class Services(View):
    def get(self,request):
        return render(request,'services.html',{})

class projets(View):
    def get(self,request):
        return render(request,'projets.html',{})

class propos(View):
    def get(self,request):
        return render(request,'propos.html',{})

class Contact(View):
    def get(self,request):
        return render(request,'Contact.html',{})


