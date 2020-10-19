from memo.ownerInfo import *
from memo.tabs import *
from memo.models import *
from memo.context import *
from django.shortcuts import render, redirect
# from memo.imageUpload import *

def newMemo(request, user_id):
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
            context = OwnerContext(user_id, request.session['user_id']).owner_context
            return render(request, 'newmemo.html', context)
        
    else:
        owner = Owner(user_id)
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
        video_url01 = request.POST['video01']
        video_url02 = request.POST['video02']
        video_url03 = request.POST['video03']
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
        if request.POST.get('style_second'):
            style_second = request.POST.get('style_second')
        if request.POST.get('style_third'):
            style_third= request.POST.get('style_third')
        
        images = Photos.objects.all()
        imgs = [''] * 4        
        for i in range(len(imgs)):
            if len(images) > i:
                imgs[i] = images[i].files

        images02 = Photos02.objects.all()
        imgs02 = [''] * 4
        for i in range(len(imgs02)):
            if len(images02) > i:
                imgs02[i] = images02[i].files

        images03 = Photos03.objects.all()
        imgs03 = [''] * 2
        for i in range(len(imgs03)):
            if len(images03) > i:
                imgs03[i] = images03[i].files     
        
        video01 = owner.YouTubeId(video_url01)
        video02 = owner.YouTubeId(video_url02)
        video03 = owner.YouTubeId(video_url03)        

        Memos.objects.create(made_by=made_by, subject=subject, content=content, content_code=content_code, language=language, desc=desc, image01=imgs[0], image02=imgs[1], image03=imgs[2] ,image04=imgs[3],image05=imgs02[0],image06=imgs[1],image07=imgs[2],image08=imgs[3],image09=imgs03[0],image10=imgs03[1], style_first=style_first, style_second=style_second, style_third=style_third, subject_2nd=subject_2nd, content_2nd=content_2nd, desc_2nd=desc_2nd, subject_3rd=subject_3rd,content_3rd=content_3rd, desc_3rd=desc_3rd, video01=video01,video02=video02, video03=video03, keyword=keyword, tab_name=tab_name, disclose=disclose, comment_on=comment_on)
        
        Photos.objects.filter(user=user_id).delete() 
        Photos02.objects.filter(user=user_id).delete() 
        Photos03.objects.filter(user=user_id).delete()

        return redirect(f'/{user_id}/') 