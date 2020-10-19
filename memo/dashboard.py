from django.shortcuts import render, redirect
from memo.models import *
from memo.loggedUser import *
from memo.ownerInfo import *
from memo.context import *
# from memo.loggedUser import *

def dashboard(request, user_id):
    owner = Owner(user_id)
    # account_owner = Users.objects.get(user_id=user_id)
    if owner is None:
        return redirect('/')

    # when a visitor comes in dashboard (non-registered)
    if 'user_id' not in request.session:
        owner.PublicYouTube                
        context = VisitorContext(user_id).visitor_context
        return render(request, 'dashboard.html', context)

    # when a registered user visits other account dashboard    
    if owner.owner.user_id != request.session['user_id']:
        owner.PublicYouTube
        context = LoggedUserContext(user_id, request.session['user_id']).logged_user_context        
        return render(request,'dashboard.html', context)
    
    # when account owner comes in his dashboard
    else:
        owner.OwnerYouTube
        context = OwnerContext(user_id, request.session['user_id']).owner_context
        return render(request, 'dashboard.html', context)