from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required,login_required
from bakery_app.forms import BakeryForm
from bakery_app.models import Product
# Create your views here.

@permission_required('admin',login_url="/")
def testHello(req):
    bakeries = Product.objects.all()
    return render(req,'dashboard.html', {'bakeries':bakeries})

@permission_required('admin',login_url="/")
@login_required
def create_bakery(req):
    if req.method == 'POST':
        form = BakeryForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BakeryForm()
    return render(req, 'create_bakery.html', {'form':form})

@login_required
def update_bakery(req,id):
    bakeries = Product.objects.get(pk=id)
    form = BakeryForm(req.POST, instance=bakeries)
    if form.is_valid():
        form.instance.owner = req.user
        form.save()
        return redirect('dashboard')
    return render(req, 'update_bakery.html', {'bakeries':bakeries})

@login_required
def delete_bakery(req,id):
    bakeries = Product.objects.get(pk=id)
    bakeries.delete()
    return redirect('dashboard')