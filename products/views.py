from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import Product
from .forms import ProductForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            product.save()
            return HttpResponseRedirect('/')

    else:
        form = ProductForm()

    template = loader.get_template('create_product.html')
    context = {
        'form': form
    }

    return HttpResponse(template.render(context, request))

def login_view(request):
    if request.method == 'POST':
        action = request.POST['action']
        username = request.POST['username']
        password = request.POST['password']

        if action == 'register':
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('/')

        elif action == 'login':
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    return render(request, 'login.html', {})

def profile(request):
    return render(request, 'profile.html', {})

# def store_home(request):
#     product = Product.objects.order_by('id')
#     template = loader.get_template('store_home.html')
#     context = {
#         'product': product
#     }
#
#     return HttpResponse(template.render(context, request))
#
# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     template = loader.get_template('product_detail.html')
#     context = {
#         'product': product
#     }
#
#     return HttpResponse(template.render(context, request))
