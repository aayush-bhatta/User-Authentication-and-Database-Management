from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login 
from .models import AuthUser  # Replace with your actual model name


# password for test user Ramesh$$$***
#     username Ramesh
  
# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")

    # Query data
 # Check if user is a superuser
    if request.user.is_superuser:
        data = AuthUser.objects.all()  # Superuser sees all users
    else:
        data = AuthUser.objects.filter(id=request.user.id)  # Regular user sees only their data
    # Pass data to the template
    return render(request, "index.html", {"data": data})


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)

        # check if us er has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
            # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
             return render(request, "login.html")


    return render(request, "login.html")

  
def logoutuser(request):
    logout(request )
    return redirect("/login")
    # return render(request, "logout.html")
    # return ("i am index page")


