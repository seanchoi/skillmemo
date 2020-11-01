from memo.ownerInfo import *
from memo.tabs import *
from memo.models import *
from memo.context import *
from django.shortcuts import render, redirect

def editMemo(request, user_id, memo_id):
    if request.method =="GET":
        user = Users.objects.filter(user_id=user_id)
        if len(user)==0:
            return redirect('/')
        owner = Owner(user_id)
        if 'user_id' not in request.session:
            return redirect(f'/{user_id}/')
        elif owner.owner.user_id != request.session['user_id']:
            return redirect(f'/{user_id}/')
        else:
            the_memo = Memos.objects.get(id=memo_id)
            context = UserMemoContext(user_id, memo_id, request.session['user_id']).memo_context
            return render(request, 'editmemo.html', context)
    else:
        owner = Owner(user_id)
        the_memo = Memos.objects.get(id=memo_id)
        made_by = Users.objects.get(user_id=user_id)
        subject = request.POST['subject']
        content = request.POST['content']
        content_code = request.POST['content_code']
        language = request.POST['language']
        desc = request.POST['desc']
        subject_2nd = request.POST['subject_2nd']
        content_2nd = request.POST['content_2nd']
        desc_2nd = request.POST['desc_2nd']
        subject_3rd = request.POST['subject_3rd']
        content_3rd = request.POST['content_3rd']
        desc_3rd = request.POST['desc']
        # cloud_link = request.POST['cloud_link']
        keyword = request.POST['keyword']
        tab_name = request.POST['tab_name']
        disclose = request.POST['disclose']
        comment_on = request.POST['comment_on']

        style_first=""
        style_second=""
        style_third=""
        if request.POST.get('style'):
            style_first = request.POST.get('style')
            the_memo.style_first = style_first
            the_memo.save()
        if request.POST.get('style_second'):
            style_second = request.POST.get('style_second')
            the_memo.style_second = style_second
            the_memo.save()
        if request.POST.get('style_third'):
            style_third= request.POST.get('style_third')    
            the_memo.style_third = style_third
            the_memo.save()

        images = Photos.objects.all()
        if len(images):
            imgs = [''] * 4        
            for i in range(len(imgs)):
                if len(images) > i:
                    imgs[i] = images[i].files
            the_memo.image01=imgs[0]
            the_memo.image02=imgs[1]
            the_memo.image03=imgs[2]
            the_memo.image04=imgs[3]
            the_memo.save()
            Photos.objects.filter(user=user_id).delete() 

        images02 = Photos02.objects.all()
        if len(images02):
            imgs02 = [''] * 4
            for i in range(len(imgs02)):
                if len(images02) > i:
                    imgs02[i] = images02[i].files
            the_memo.image05=imgs02[0]
            the_memo.image06=imgs02[1]
            the_memo.image07=imgs02[2]
            the_memo.image08=imgs02[3]
            the_memo.save()
            Photos02.objects.filter(user=user_id).delete() 

        images03 = Photos03.objects.all()
        if len(images02):
            imgs03 = [''] * 2
            for i in range(len(imgs03)):
                if len(images03) > i:
                    imgs03[i] = images03[i].files   
            the_memo.image09=imgs03[0]
            the_memo.image10=imgs03[1]
            the_memo.save()
            Photos03.objects.filter(user=user_id).delete()

        v01 = ""
        v02 = ""
        v03 = ""
        if request.POST['video01']:
            v01 = owner.YouTubeId(request.POST['video01'])
            the_memo.video01 = v01
            the_memo.save()
        if request.POST['video02']:
            v02 = owner.YouTubeId(request.POST['video02'])
            the_memo.video02 = v02
            the_memo.save()
        if request.POST['video03']:
            v03 = owner.YouTubeId(request.POST['video03'])  
            the_memo.video03 = v03
            the_memo.save()

        the_memo.subject = subject
        the_memo.content = content
        the_memo.content_code = content_code
        the_memo.language = language
        the_memo.desc = desc
        the_memo.subject_2nd = subject_2nd
        the_memo.content_2nd = content_2nd
        the_memo.desc_2nd = desc_2nd
        the_memo.subject_3rd = subject_3rd
        the_memo.content_3rd = content_3rd
        the_memo.desc_3rd = desc_3rd
        the_memo.keyword = keyword
        the_memo.tab_name = tab_name
        the_memo.disclose = disclose
        the_memo.comment_on = comment_on
        the_memo.save()
        
        return redirect(f'/{user_id}/{memo_id}/')