import bcrypt
import re
from django.shortcuts import render, redirect
from memo.models import Users
from django.contrib import messages

# REGISTRATION PAGE
# registration form validation by ajax
# email check with re (REGEX)
# password encode by bcrypt

def nameCheck(request, name):
    found = ""
    data = request.POST[f'{name}']    
    if len(data) == 0:
        found = "required"
    if len(data) > 0 and len(data) < 2:
        found = "short"        
        for i in range(len(data)):
            if not data[i].isalpha():
                found = True
    else:
        for i in range(len(data)):
            if not data[i].isalpha():
                found = True         
    context = {
        'found' : found
    }
    return render(request, 'partials/name.html', context)

def emailCheck(request):
    found = False
    data = request.POST['email']
    if len(data) == 0:
        found = "required"    
    if len(data)>0:
        found="nothing"        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(data):
            found = "not valid"
        else:
            users = Users.objects.filter(email=data)    
            if len(users):
                found = "duplicate"
            else:
                found=False
    context = {
        'found' : found,
    }
    return render(request, 'partials/email.html', context)

def userIdCheck(request):
    data = request.POST['user_id']
    users = Users.objects.filter(user_id=data)    
    found = ""
    if len(data) == 0:
        found = "required"
    if len(data) > 0 and len(data) < 4:
        found = "short"
    elif len(data) > 4:
        found = False
        if len(users):
            found = True
        else:
            found = False
    context = {
        'found' : found
    }
    return render(request, 'partials/user_id.html', context)

def passwordCheck(request):
    data = request.POST['password']
    found = ""
    if len(data) == 0:
        found = "required"
    if len(data) > 0 and len(data)< 6:
        found = "short"
    elif len(data) > 6:
        found = False
    context = {
        'found' : found
    }
    return render(request, 'partials/pass.html', context)

# registration
def register(request):
    if request.method == "POST":
        errors = Users.objects.validator(request.POST)
        if len(errors):
            for key, val in errors.items():
                messages.error(request, val)
                return redirect('/register')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user_id = request.POST['user_id'].lower()
            email = request.POST['email']
            password = request.POST['password']            
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = Users.objects.create(first_name=first_name, last_name=last_name, user_id=user_id, email=email, password=pw_hash)                      
            return redirect('/login')
    return render(request, 'register.html')

# LOGIN PAGE
def loginIdCheck(request):
    data = request.POST['user_id']
    users = Users.objects.filter(user_id=data)
    found = ""
    if len(data) == 0:
        found = "required"    
    if users:
        found = True
    else:
        found = False
    context = {
        'found' : found
    }
    return render(request, 'partials/login_id.html', context)

def login(request):
    if request.method == "POST":
        user = Users.objects.filter(user_id=request.POST['user_id'].lower())
        if len(user):
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.user_id
                return redirect(f'/{user[0].user_id}/')
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('/')