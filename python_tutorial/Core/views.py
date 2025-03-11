from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, SignInForm

def home(request):
    return render(request, "Core/index.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            fname = form.cleaned_data["fname"]
            lname = form.cleaned_data["lname"]
            email = form.cleaned_data["email"]
            pass1 = form.cleaned_data["pass1"]

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.Please choose different username")
                return redirect("signup")
            
            if User.objects.filter(email = email).exists():
                messages.error(request, "Email is already exits.")
                return redirect("signup")

            # Create user
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()

            messages.success(request, "Your account has been successfully created.")
            return redirect("signin")
        else:
            messages.error(request, "There was an error with the form.")
    
    else:
        form = SignUpForm() 

    return render(request, "Core/signup.html", {"form": form})

def signin(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            pass1 = form.cleaned_data["pass1"]

            user = authenticate(username=username, password=pass1)

            if user is not None:
                login(request, user)
                fname = user.first_name
                return render(request, "Core/index.html", {"fname": fname})
            else:
                messages.error(request, "Invalid credentials.")
                return redirect("signin")
        else:
            messages.error(request, "There was an error with the form.")
    else:
        form = SignInForm()

    return render(request, "Core/signin.html", {"form": form})

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Successfully Logged Out")
    else:
        messages.info(request, "You are not logged in ")

    return redirect('home')
