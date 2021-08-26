from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . helpers import send_forgot_pass_mail
from accounts.models import Profile
import uuid


# Logging User in
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Welcome! Now you are logged in')
            return redirect("/")
        else:
            messages.error(request,'Username/Password is not correct !')
            return render(request,'login.html')

    else:
        return render(request,'login.html')

# Registering User
def reg_user(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password1')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request,'Username is already taken !')
            return render(request, 'register.html')
        if pass1 != pass2:
            messages.error(request,'Passwords must be same !')
            return render(request, 'register.html')
        if pass1 == pass2:
            user1 = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=pass1)
            messages.success(request,'You have registered yourself seccussfully! Please Sign in now ')
            user1.save()
            return redirect("/login")
    else:
        return render(request, 'register.html')

# Logging User Out
def logout_user(request):
    logout(request)
    return redirect("/")

# Password Reset
def password_reset(request):
    if request.method == "POST":
        email = request.POST.get('email')
        token = str(uuid.uuid4())

        user = User.objects.get(email=email)
        if user is not None:
            send_forgot_pass_mail(email, token)
            userid = user.id
            userobj = User.objects.get(id=userid)
            profile = Profile(user=userobj, forgot_password_token = token)
            profile.save()
            messages.success(request,'Email has been sent! Please check your email inbox')
            return render(request, 'password_reset.html')
        
        if user is None:
            messages.error(request,'Email did not matched. Kindly recheck your email address')
            return render(request, 'password_reset.html')
       
    else:
        return render(request, 'password_reset.html')
        
# Forgot User Password
def forgot_password(request, token):   
    profile_obj = Profile.objects.filter(forgot_password_token = token).first()
    #print(profile_obj)
    context = {
        'user_id' : profile_obj.user.id,
        'token' : token
    }
    
    if request.method == "POST":
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password1')
        userid = request.POST.get('user_id')

        if userid is not None:
            if pass1 == pass2:
                user =User.objects.get(id=userid)
                user.set_password(pass1)
                user.save()
                messages.success(request,'Your password has been updated successfully !')
                return redirect(f'/forgot_password/{token}/')
            else:
                messages.error(request,'Passwords must be same')
                return redirect(f'/forgot_password/{token}/')
        else:
            messages.error(request,'Something went wrong. Please reopen password reset link')
            return redirect(f'/forgot_password/{token}/')

    return render(request, 'forgot_password.html', context)
