from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from bakery_app.models import Product
# Create your views here.

@permission_required('admin',login_url="/")
def testHello(req):
    bakeries = Product.objects.all()
    return render(req,'dashboard.html', {'bakeries':bakeries})