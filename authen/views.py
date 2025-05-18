from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import myuser
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
User = get_user_model()


def signUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['mail']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        if User.objects.filter(username=username):
            messages.error(request,"Username already exist!")
            return redirect('signUp')
        if User.objects.filter(email=email):
            messages.error(request,"Email already exist!")
            return redirect('signUp')
        
        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")
            return redirect('signUp')
        if password!=conpassword:
            messages.error(request,"Passwords did not match")
            return redirect('signUp')
        if not  username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('signUp')

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=username
        myuser.save()
        return redirect('main')

    return render(request,"signUp.html")

def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if(User.objects.filter(username=username)):
            user = User.objects.get(username=username)
            password_valid = user.check_password(password)

            if password_valid :
                if user is not None:
                    user = authenticate(username=user.username, password=password)
                    login(request,user)
                    return redirect('main')
                else:
                    return redirect('signIn')
            else:
                messages.error(request,"Passwords is not valid")
                return redirect('signIn')
    
        else:
            messages.error(request, "Username Innvalid")
            return redirect('signIn')

    return render(request, 'signIn.html')


def signOut(request):
    logout(request)
    return redirect('main')

def viewProfile(request):
    if request.method == 'POST':
        use = User.objects.get(username=request.user.username)
        use.username = request.POST.get('username')
        use.email = request.POST.get('email')
        use.save()
        return redirect(request.META['HTTP_REFERER'])

    return render(request, "viewProfile.html")

def deleteAccount(request):
    User.objects.filter(username=request.user.username).delete()
    
    return redirect('singOut')