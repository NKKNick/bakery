from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
# Create your views here.
def login(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        if username == "" or password=="":
            return redirect("/login")
        else:
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(req,user)
                return redirect('/')
            else:
                return redirect('/login')
    return render(req,'login.html')

def register(req):
    if req.method == "POST":
        username = req.POST["username"]
        email = req.POST["email"]
        password = req.POST["password"]
        password2 = req.POST["password2"]
        if username=='' or email=='' or password=='' or password2=='':
            return redirect("/register")
        elif password != password2:
            return redirect("/register")
        else:
            if User.objects.filter(username=username).exists():
                return redirect("/register")
            else:
                user=User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                return redirect("/register")
    return render(req,'register.html')
def logout(req):
    auth.logout(req)
    return redirect("/")