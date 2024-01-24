from django.shortcuts import render, redirect
from bakery_app.forms import BakeryForm
from bakery_app.models import Product

# Create your views here.
def index(req):
    return render(req, "index.html")

def show_bakery(req):
    bakeries = Product.objects.all()
    return render(req, 'show_bakery.html', {'bakeries':bakeries})

def create_bakery(req):
    form = BakeryForm
    if req.method == 'POST':
        form = BakeryForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('show_bakery')
    return render(req, 'create_bakery.html', {'form':form})

def update_bakery(req,id):
    bakeries = Product.objects.get(pk=id)
    form = BakeryForm(req.POST, instance=bakeries)
    if form.is_valid():
        form.instance.owner = req.user
        form.save()
        return redirect('show_bakery')
    return render(req, 'update_bakery.html', {'fic':bakeries})

def delete_bakery(req,id):
    bakeries = Product.objects.get(pk=id)
    bakeries.delete()
    return redirect('show_bakery')