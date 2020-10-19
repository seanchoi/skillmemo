from memo.models import *
from memo.ownerInfo import *
from memo.tabs import *
# context infotmation class by user status(visitor, logged user, account owner)
class VisitorContext:
    def __init__(self, user_id):
        self.owner = Users.objects.get(user_id=user_id)
        self.owner_info = Owner(user_id)
        self.context_memos = Memos.objects.filter(made_by=self.owner, disclose="public").exclude(tab_name="TRASH")  
        self.visitor_context = {
            'account_owner':self.owner,
            'account_owner_public_memos':self.context_memos[:50],
            'account_owner_memos_count':self.context_memos.count,
            'over_time_public_memos':self.owner_info.overTimePublicMemos,
            'crumbs':self.owner_info.PublicCrumbs,
        }

class LoggedUserContext:
    def __init__(self, user_id, logged_user_id):
        self.owner = Users.objects.get(user_id=user_id)
        self.owner_info = Owner(user_id)
        self.logged_user = Tabs(logged_user_id)
        self.context_memos = Memos.objects.filter(made_by=self.owner, disclose="public").exclude(tab_name="TRASH")
        saved_memos = Memos.objects.filter(users=self.logged_user.user)        
        dms_got = DMs.objects.filter(to=self.logged_user.user)
        dms_got_nocheck = DMs.objects.filter(to=self.logged_user.user, if_to_checked="no")
        dms_got_noReplyCheck = DMs.objects.filter(to=self.logged_user.user, if_to_reply_checked="no")
        dms_sent = DMs.objects.filter(sent_by=self.owner)
        dms_sent_noReplyCheck = DMs.objects.filter(sent_by=self.logged_user.user, if_from_reply_checked="no")
        dms_notificaion_count = len(dms_got_nocheck) + len(dms_got_noReplyCheck) + len(dms_sent_noReplyCheck)
        self.logged_user_context = {
            'account_owner':self.owner,
            'account_owner_memos_count':self.context_memos.count,
            'account_owner_public_memos':self.context_memos[:50],
            'over_time_public_memos':self.owner_info.overTimePublicMemos,
            'crumbs':self.owner_info.PublicCrumbs,
            'logged_user':self.logged_user.user,
            'tab01':self.logged_user.tab01,
            'tab02':self.logged_user.tab02,
            'tab03':self.logged_user.tab03,
            'tab04':self.logged_user.tab04,
            'tab05':self.logged_user.tab05,
            'dms_got':dms_got,
            'dms_got_nocheck':dms_got_nocheck,
            'dms_got_noReplyCheck':dms_got_noReplyCheck,
            'dms_sent':dms_sent,
            'dms_sent_noReplyCheck':dms_sent_noReplyCheck,
            'dms_notification_count': dms_notificaion_count,
            'saved_memos':saved_memos,
        }

class OwnerContext:
    def __init__(self, user_id,logged_user_id):
        self.owner = Users.objects.get(user_id=user_id)
        self.owner_info = Owner(user_id)
        self.logged_user = Tabs(logged_user_id)
        self.context_memos = Memos.objects.filter(made_by=self.owner).exclude(tab_name="TRASH")
        self.imgList01 = Photos.objects.filter(user=user_id)
        self.imgList02 = Photos.objects.filter(user=user_id)
        self.imgList03 = Photos.objects.filter(user=user_id)
        self.deleted = Memos.objects.filter(tab_name="TRASH")
        saved_memos = Memos.objects.filter(users=self.owner)            
        dms_got = DMs.objects.filter(to=self.owner)
        dms_got_nocheck = DMs.objects.filter(to=self.owner_info.owner, if_to_checked="no")
        dms_got_noReplyCheck = DMs.objects.filter(to=self.owner_info.owner, if_to_reply_checked="no")
        dms_sent = DMs.objects.filter(sent_by=self.owner)
        dms_sent_noReplyCheck = DMs.objects.filter(sent_by=self.owner_info.owner, if_from_reply_checked="no")
        dms_notificaion_count = len(dms_got_nocheck) + len(dms_got_noReplyCheck) + len(dms_sent_noReplyCheck)
        self.owner_context = {
            'account_owner':self.owner,
            'account_owner_memos_count':self.context_memos.count,
            'account_owner_memos':self.context_memos[:30],
            'over_time_memos':self.owner_info.overTimeMemos,
            'crumbs':self.owner_info.PublicCrumbs,
            'logged_user':self.logged_user.user,
            'tab01':self.logged_user.tab01,
            'tab02':self.logged_user.tab02,
            'tab03':self.logged_user.tab03,
            'tab04':self.logged_user.tab04,
            'tab05':self.logged_user.tab05,
            'section01_images': self.imgList01,
            'section02_images': self.imgList02,
            'section03_images': self.imgList03,
            'deleted':self.deleted,
            'dms_got':dms_got,
            'dms_got_nocheck':dms_got_nocheck,
            'dms_got_noReplyCheck':dms_got_noReplyCheck,
            'dms_sent':dms_sent,
            'dms_sent_noReplyCheck':dms_sent_noReplyCheck,
            'dms_notification_count': dms_notificaion_count,
            'saved_memos':saved_memos,
        }

class VisitorMemoContext:
    def __init__(self, user_id, memo_id):
        self.owner = Users.objects.get(user_id=user_id)
        self.owner_info = Owner(user_id)
        self.context_memos = Memos.objects.filter(made_by=self.owner)
        self.the_memo = Memos.objects.get(made_by=self.owner, id=memo_id)
        self.comments = Comments.objects.filter(reply_to=self.the_memo)
        self.memo_context = {
            'account_owner':self.owner,
            'account_owner_memos_count':self.context_memos.count,
            'the_memo':self.the_memo,
            'comments':self.comments
        }

class UserMemoContext:
    def __init__(self, user_id, memo_id, logged_user_id):
        self.owner = Users.objects.get(user_id=user_id)
        self.owner_info = Owner(user_id)
        self.logged_user = Tabs(logged_user_id)
        self.context_memos = Memos.objects.filter(made_by=self.owner).exclude(tab_name="TRASH")
        self.the_memo = Memos.objects.get(made_by=self.owner, id=memo_id)
        self.comments = Comments.objects.filter(reply_to=self.the_memo)
        saved_memos = Memos.objects.filter(users=self.logged_user.user)    
        dms_got = DMs.objects.filter(to=self.logged_user.user)
        dms_got_nocheck = DMs.objects.filter(to=self.logged_user.user, if_to_checked="no")
        dms_got_noReplyCheck = DMs.objects.filter(to=self.logged_user.user, if_to_reply_checked="no")
        dms_sent = DMs.objects.filter(sent_by=self.logged_user.user)
        dms_sent_noReplyCheck = DMs.objects.filter(sent_by=self.logged_user.user, if_from_reply_checked="no")
        dms_notificaion_count = len(dms_got_nocheck) + len(dms_got_noReplyCheck) + len(dms_sent_noReplyCheck)
        self.memo_context = {
            'account_owner':self.owner,
            'logged_user':self.logged_user.user,
            'account_owner_memos_count':self.context_memos.count,
            'the_memo':self.the_memo,
            'crumbs':self.owner_info.PublicCrumbs,
            'tab01':self.logged_user.tab01,
            'tab02':self.logged_user.tab02,
            'tab03':self.logged_user.tab03,
            'tab04':self.logged_user.tab04,
            'tab05':self.logged_user.tab05,
            'comments':self.comments,
            'dms_got':dms_got,
            'dms_got_nocheck':dms_got_nocheck,
            'dms_got_noReplyCheck':dms_got_noReplyCheck,
            'dms_sent':dms_sent,
            'dms_sent_noReplyCheck':dms_sent_noReplyCheck,
            'dms_notification_count': dms_notificaion_count,
            'saved_memos':saved_memos,
        }

class OwnerMemoContext:
    def __init__(self, user_id, memo_id, logged_user_id):
        self.owner = Users.objects.get(user_id=user_id)        
        self.owner_info = Owner(user_id)
        self.logged_user = Tabs(logged_user_id)
        self.context_memos = Memos.objects.filter(made_by=self.owner).exclude(tab_name="TRASH")
        self.the_memo = Memos.objects.get(made_by=self.owner, id=memo_id)
        self.comments = Comments.objects.filter(reply_to=self.the_memo)
        dms_got = DMs.objects.filter(to=self.logged_user.user)
        dms_got_nocheck = DMs.objects.filter(to=self.logged_user.user, if_to_checked="no")
        dms_got_noReplyCheck = DMs.objects.filter(to=self.logged_user.user, if_to_reply_checked="no")
        dms_sent = DMs.objects.filter(sent_by=self.logged_user.user)
        dms_sent_noReplyCheck = DMs.objects.filter(sent_by=self.logged_user.user, if_from_reply_checked="no")
        dms_notificaion_count = len(dms_got_nocheck) + len(dms_got_noReplyCheck) + len(dms_sent_noReplyCheck)
        self.memo_context = {
            'account_owner':self.owner,
            'logged_user':self.logged_user.user,   
            'account_owner_memos_count':self.context_memos.count,
            'the_memo':self.the_memo,
            'crumbs':self.owner_info.PublicCrumbs,
            'tab01':self.logged_user.tab01,
            'tab02':self.logged_user.tab02,
            'tab03':self.logged_user.tab03,
            'tab04':self.logged_user.tab04,
            'tab05':self.logged_user.tab05,
            'comments':self.comments,
            'dms_got':dms_got,
            'dms_got_nocheck':dms_got_nocheck,
            'dms_got_noReplyCheck':dms_got_noReplyCheck,
            'dms_sent':dms_sent,
            'dms_sent_noReplyCheck':dms_sent_noReplyCheck,
            'dms_notification_count': dms_notificaion_count,
        }