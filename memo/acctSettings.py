from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from memo.models import *
from memo.ownerInfo import *
from memo.context import *
# from memo.tabTheme import *
import bcrypt

def settings(request, user_id):
    if request.method =="GET":
        user = Users.objects.filter(user_id=user_id)
        if len(user)==0:
            return redirect('/')
        owner = Owner(user_id)
        if owner.owner.user_id !=user_id or 'user_id' not in request.session:
            return redirect('/')
        else:
            context = OwnerContext(user_id, request.session['user_id']).owner_context
            return render(request, 'settings.html', context)
    else:
        owner = Owner(user_id)
        first_name = request.POST['first_name']
        brand_name = request.POST['brand_name']
        brand_desc = request.POST['brand_desc']
        view_mode = request.POST['view_mode']
        tab_view = request.POST['tab_view']
        tab_theme = request.POST['tab_theme']
        email = request.POST['email']
        tab01 = request.POST['tab01']
        tab02 = request.POST['tab02']
        tab03 = request.POST['tab03']
        tab04 = request.POST['tab04']
        tab05 = request.POST['tab05']
        
        profile_pic = ""
        if request.FILES.get('profile_pic'):
            owner.owner.profile_pic.delete()
            profile_pic = request.FILES.get('profile_pic')
            owner.owner.profile_pic = profile_pic
            owner.owner.save()
            # storage = FileSystemStorage()
            # filename = storage.save(profile_pic.name, profile_pic)
            # image = storage.usr(filename)

        pw_hash = ""
        if request.POST['password']:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            owner.owner.password = pw_hash
            owner.owner.save()
        owner.owner.first_name = first_name
        owner.owner.brand_name = brand_name
        owner.owner.brand_desc = brand_desc
        owner.owner.view_mode = view_mode
        owner.owner.tab_view = tab_view
        owner.owner.tab_theme = tab_theme
        owner.owner.email = email        
        Memos.objects.filter(made_by=owner.owner, tab_name=owner.owner.tab01).update(tab_name=tab01)
        owner.owner.tab01 = tab01
        Memos.objects.filter(made_by=owner.owner, tab_name=owner.owner.tab02).update(tab_name=tab02)
        owner.owner.tab02 = tab02
        Memos.objects.filter(made_by=owner.owner, tab_name=owner.owner.tab03).update(tab_name=tab04)
        owner.owner.tab03 = tab03
        Memos.objects.filter(made_by=owner.owner, tab_name=owner.owner.tab04).update(tab_name=tab04)
        owner.owner.tab04 = tab04
        Memos.objects.filter(made_by=owner.owner, tab_name=owner.owner.tab05).update(tab_name=tab05)
        owner.owner.tab05 = tab05
        owner.owner.save()

        # #tab color theme
        # theme = TabTheme(user_id, tab_theme)
        return redirect(f'/{user_id}/settings/')