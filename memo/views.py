from django.shortcuts import render, redirect
from django.contrib import messages
from memo.loginReg import *
from memo.models import *
from memo.ownerInfo import *
from memo.context import *
from memo.newMemo import newMemo
from memo.editMemo import editMemo
from memo.imageSave import *
from memo.searchPreview import *
from memo.search import *
from memo.crumbSearch import *
from memo.acctSettings import *
import bcrypt
from datetime import datetime, timedelta
from django.http import JsonResponse
from .forms import *
from django.core.files.storage import FileSystemStorage

def index(request):
    if 'user_id' in request.session:      
        user_id = request.session['user_id']  
        return redirect(f'/{user_id}/')
    return render(request,'index.html')     

def dashboard(request, user_id):
    user = Users.objects.filter(user_id=user_id)
    if len(user)==0:
        return redirect('/')
    owner = Owner(user_id)    
    # when a visitor comes in dashboard (non-registered)
    if 'user_id' not in request.session:              
        context = VisitorContext(user_id).visitor_context
    # when a registered user visits other account dashboard    
    elif owner.owner.user_id != request.session['user_id']:
        context = LoggedUserContext(user_id, request.session['user_id']).logged_user_context        
    # when account owner comes in his dashboard
    else:
        OwnerContext(user_id, request.session['user_id']).checkNewComments()
        context = OwnerContext(user_id, request.session['user_id']).owner_context
    return render(request, 'dashboard.html', context)

def viewMemo(request, user_id, memo_id):
    user = Users.objects.filter(user_id=user_id)
    if len(user)==0:
        return redirect('/')
    owner = Owner(user_id)
    the_memo = Memos.objects.get(id=memo_id)
    if 'user_id' not in request.session:
        if the_memo.disclose == "private":
            return redirect(f'/{user_id}/')
        context = VisitorMemoContext(user_id, memo_id).memo_context
    elif owner.owner.user_id != request.session['user_id']:
        if the_memo.disclose == "private":
            return redirect(f'/{user_id}/')
        context = UserMemoContext(user_id, memo_id, request.session['user_id']).memo_context
    else:
        the_memo.if_new_comment = "no"
        the_memo.save()
        context = OwnerMemoContext(user_id, memo_id, request.session['user_id']).memo_context
    return render(request,'viewmemo.html', context)

def comment(request, user_id, memo_id):
    if request.method == "GET":
        return redirect(f'/{user_id}/{memo_id}')    
    else:
        name = request.POST['name']
        content = request.POST['content']
        reply_by_dashboard = request.POST['reply_by_dashboard']
        reply_by_profile_pic = request.POST['reply_by_profile_pic']    
        reply_to = Memos.objects.get(id=memo_id)
        Comments.objects.create(name=name, content=content, reply_to=reply_to, reply_by_dashboard=reply_by_dashboard, reply_by_profile_pic=reply_by_profile_pic)
        return redirect(f'/{user_id}/{memo_id}')

def deleteComment(request,user_id, memo_id, comment_id):
    if request.method == "POST":
        Comments.objects.get(id=comment_id).delete()
        return redirect(f'/{user_id}/{memo_id}')
    else:
        return redirect(f'/{user_id}/{memo_id}')

def profilePicDelete(request, user_id):
    user = Users.objects.filter(user_id=user_id)
    if len(user)==0:
        return redirect('/')
    owner = Owner(user_id)
    if owner.owner.user_id != user_id or 'user_id' not in request.session:
        return redirect('/')
    else:
        owner.owner.profile_pic.delete()
        return redirect(f'/{user_id}/settings/')

def searchPreview(request, user_id): # preview on search bar by ajax
    # owner = Owner(user_id)
    search_keyword = ""
    session = ""
    if 'user_id' in request.session:
        session = request.session['user_id']
    if request.method == "POST":
        if request.POST['search']:
            search_keyword = request.POST['search']
            if search_keyword[0] == "@":
                if not search_keyword[0]:
                    return render(request,'partials/search_users.html')
                else:
                    context = SearchPreview(user_id, search_keyword, session).context
                    return render(request, 'partials/search_users.html', context)
            else:
                context = SearchPreview(user_id, search_keyword, session).context
                return render(request, 'partials/search_memos.html', context)
        else:
            return render(request,'partials/search_memos.html')

def search(request, user_id):
    # owner = Owner(user_id)
    session = ""
    if 'user_id' in request.session:
        session = request.session['user_id']
    if request.method == "POST":
        if request.POST['search']:
            search_keyword = request.POST['search']
            if search_keyword[0] == "@":
                search_keyword = search_keyword[1:]
                if search_keyword[1:] == "":
                    return redirect(f'/{user_id}/')
                else: 
                    user = Users.objects.get(user_id=search_keyword)
                    if not user:
                        return redirect(f'/{user_id}/')
                    else:
                        return redirect(f'/{user.user_id}/')
            else:
                context = Search(user_id, search_keyword, session).context
                return render(request, 'search_result.html', context)   

def searchByCrumb(request, user_id, keyword): 
    session = ""
    if 'user_id' in request.session:
        session = request.session['user_id']
    context = crumbSearch(user_id, keyword, session).context
    return render(request, 'search_result.html', context)

def moveMemoToTrash(request, user_id, memo_id):
    if request.method == "POST":
        the_memo = Memos.objects.get(id=memo_id)
        user = Users.objects.get(user_id=user_id)
        the_memo.tab_name = user.tab06
        the_memo.save()       
        return redirect(f'/{user_id}/')
    return redirect(f'/{user_id}')

def reAssignTab(request, user_id, memo_id):
    if request.method == "POST":
        the_memo = Memos.objects.get(id=memo_id)
        user = Users.objects.get(user_id=user_id)
        tab = request.POST['move_to']
        the_memo.tab_name = tab
        the_memo.save()
        return redirect(f'/{user_id}')
    return redirect(f'/{user_id}')

def deleted(request, user_id):
    if request.method =="GET":
        user = Users.objects.filter(user_id=user_id)
        if len(user)==0:
            return redirect('/')
        owner = Owner(user_id)
        if owner.owner.user_id !=user_id or 'user_id' not in request.session:
            return redirect('/')
        else:
            context = OwnerContext(user_id, request.session['user_id']).owner_context
            return render(request, 'deleted.html', context)

def memoPermanentDelete(request, user_id, memo_id):
    if request.method == "POST":
        owner = Users.objects.get(user_id=user_id)
        Memos.objects.get(made_by=owner, id=memo_id).delete()
    return redirect(f'/{user_id}/deleted_memos/')

def sendDm(request, user_id):
    if request.method == "POST":  
        errors = DMs.objects.validator(request.POST)
        if len(errors):
            for key, val in errors.items():
                messages.error(request, val)
                return redirect(f'/{user_id}/dm_fail/')      
        else:
            to = Users.objects.get(user_id=request.POST['to'])
            sent_by = Users.objects.get(user_id=request.POST['from_user_id'])
            to_user_id = to.user_id
            from_user_id = request.POST['from_user_id']
            dm_msg = request.POST['dm_msg']
            DMs.objects.create(to=to, sent_by=sent_by,to_user_id = to_user_id,from_user_id=from_user_id, dm_msg=dm_msg)            
            return redirect(f'/{user_id}/')
    else:
        return redirect(f'/{user_id}/')

def dmFail(request, user_id):
    context = OwnerContext(user_id, request.session['user_id']).owner_context
    return render(request, 'dm_fail.html', context)

def viewMessages(request, user_id):
    if request.method =="GET":
        user = Users.objects.filter(user_id=user_id)
        if len(user) == 0:
            return redirect('/')
        owner = Owner(user_id)
        if 'user_id' not in request.session:
            return redirect('/')
        else:
            logged_user = Users.objects.get(user_id=request.session['user_id'])
            if logged_user.user_id != user_id:
                return redirect('/')
            else:
                context = OwnerContext(user_id, request.session['user_id']).owner_context
                return render(request, 'messages.html', context)

def checkDm(request, user_id, dm_id):
    if request.method=="GET":
        if request.method =="GET":
            user = Users.objects.filter(user_id=user_id)
        if len(user) == 0:
            return redirect('/')
        owner = Owner(user_id)
        if 'user_id' not in request.session:
            return redirect('/')
        else:
            logged_user = Users.objects.get(user_id=request.session['user_id'])
            if logged_user.user_id != user_id:
                return redirect('/')
            else:
                check=DMs.objects.get(id=dm_id)
                if check.to_user_id == user_id:
                    check.if_to_checked ="yes"
                    check.if_to_reply_checked="yes"
                else: 
                    check.if_from_reply_checked="yes"
                check.save()
                context = OwnerContext(user_id, request.session['user_id']).owner_context
                context['dm'] = DMs.objects.get(id=dm_id)
                context['sender'] = Users.objects.get(user_id=context['dm'].from_user_id)
                context['dmReply'] = DmReply.objects.filter(reply_for=context['dm'])
                return render(request, 'dm.html', context)

def replyDm(request, parent_dm_id, reply_user_id):
    if request.method == "POST":        
        reply_for = DMs.objects.get(id=request.POST['parent_dm_id'])
        parent_dm_id = request.POST['parent_dm_id']
        reply_user_id = request.POST['reply_user_id']
        reply_name = Users.objects.get(user_id=reply_user_id).first_name
        reply_msg = request.POST['reply_msg']
        
        parent_dm = DMs.objects.get(id=parent_dm_id)
        if parent_dm.to_user_id == reply_user_id:    
            parent_dm.if_from_reply_checked = "no"
        else: 
            parent_dm.if_to_reply_checked = "no"
        parent_dm.save()
        DmReply.objects.create(reply_for=reply_for, parent_dm_id=parent_dm_id, reply_user_id=reply_user_id, reply_name=reply_name, reply_msg=reply_msg)        
        context = OwnerContext(reply_user_id, request.session['user_id']).owner_context
        return redirect(f'/{reply_user_id}/{parent_dm_id}/check_dm/')
    else:
        return redirect(f'/{reply_user_id}/')

def deleteDm(request,user_id, dm_id):
    if request.method == "POST":        
        dm = DMs.objects.get(id=dm_id).delete()
        return redirect(f'/{user_id}/messages/')
    else:
        return redirect(f'/{user_id}/')

def deleteAccount(request, user_id):
    if request.method == "POST":
        user = Users.objects.get(user_id=user_id)
        user.delete()
        request.session.flush()
        return redirect('/')
    return redirect('/')

def memoSave(request,account_id,user_id, memo_id):
    if request.method == "POST":      
        memo = Memos.objects.get(id=memo_id)
        user = Users.objects.get(user_id=user_id)
        user.saved.add(memo)
        return redirect(f'/{account_id}/')

def memoUnSave(request, account_id, user_id, memo_id):
    if request.method == "POST":
        memo = Memos.objects.get(id=memo_id)
        user = Users.objects.get(user_id=user_id)
        user.saved.remove(memo)
        return redirect(f'/{account_id}/')

def savedMemo(request, user_id):
    if request.method =="GET":
        user = Users.objects.filter(user_id=user_id)
        if len(user)==0:
            return redirect('/')
        owner = Owner(user_id)
        if owner.owner.user_id !=user_id or 'user_id' not in request.session:
            return redirect('/')
        else:
            context = OwnerContext(user_id, request.session['user_id']).owner_context
            return render(request, 'savedmemo.html', context)

def contact(request, user_id):
    if 'user_id' not in request.session:
        context = VisitorContext(user_id).visitor_context
        return render(request, 'contact.html', context)
    else:
        context = LoggedUserContext(user_id, request.session['user_id']).logged_user_context
        return render(request,'contact.html', context)
