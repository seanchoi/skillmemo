from memo.models import *
# logged user information class
class Tabs:
    def __init__(self, user_id):
        self.user = Users.objects.get(user_id=user_id)
        self.user_id = user_id
        self.tab01 = Memos.objects.filter(made_by=self.user, tab_name=self.user.tab01)
        self.tab02 = Memos.objects.filter(made_by=self.user, tab_name=self.user.tab02)
        self.tab03 = Memos.objects.filter(made_by=self.user, tab_name=self.user.tab03)
        self.tab04 = Memos.objects.filter(made_by=self.user, tab_name=self.user.tab04)
        self.tab05 = Memos.objects.filter(made_by=self.user, tab_name=self.user.tab05)
