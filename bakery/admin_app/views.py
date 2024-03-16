from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required,login_required
from bakery_app.forms import BakeryForm
from bakery_app.models import Product
from user_order.models import Order, OrderDetail
# Create your views here.

@permission_required('admin',login_url="/")
def testHello(req):
    bakeries = Product.objects.all()
    return render(req,'dashboard.html', {'bakeries':bakeries})

@permission_required('admin',login_url="/")
def create_bakery(req):
    if req.method == 'POST':
        form = BakeryForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BakeryForm()
    return render(req, 'create_bakery.html', {'form':form})

@permission_required('admin',login_url="/")
def update_bakery(req,id):
    if req.method == "POST":       
        bakeries = Product.objects.get(pk=id)
        form = BakeryForm(req.POST,req.FILES,instance=bakeries)
        if form.is_valid():
            form.instance.owner = req.user
            form.save()
            return redirect('dashboard')
    else:
        bakeries = Product.objects.get(pk=id)
        form = BakeryForm(instance=bakeries)
    return render(req, 'update_bakery.html', {'bakeries':bakeries,'form':form})

@permission_required('admin',login_url="/")
def delete_bakery(req,id):
    bakeries = Product.objects.get(pk=id)
    bakeries.delete()
    return redirect('dashboard')

def order_admin(req):
    order = Order.objects.all()
    return render(req,'order_admin.html',{'order':order})

def orderdetail_admin(req,id):
    order = Order.objects.get(pk=id)
    detail = OrderDetail.objects.filter(order=order)
    return render(req,'orderdetail_admin.html',{'detail':detail,'order':order}) 

def update_status(req,id):
    order = Order.objects.get(pk=id)
    if req.method == "POST":
        order.status = req.POST['status']
        order.save()
        return redirect("/dashboard/order_admin")
        
    