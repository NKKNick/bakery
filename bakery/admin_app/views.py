from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
# Create your views here.

@permission_required('admin',login_url="/")
def testHello(req):
    return render(req,'dashboard.html')