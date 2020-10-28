from memo.models import Users, Memos
class SearchPreview:
    def __init__(self, user_id, search_keyword, session):
        self.account_owner = Users.objects.get(user_id=user_id)
        self.keyword = search_keyword
        self.session = session
        if self.keyword[0] == "@":
            self.keyword = self.keyword[1:]
            self.users = Users.objects.filter(user_id__icontains=self.keyword).order_by('user_id',)
            self.context = {
                'search':self.users
            }
        elif self.keyword[0] == "!":
            self.keyword = self.keyword[1:]
            if self.account_owner.user_id != session:
                self.memos = Memos.objects.filter(made_by=self.account_owner, disclose="public", keyword__icontains=self.keyword).exclude(tab_name="TRASH")
                self.context = {
                    'search':self.memos
                }
            else:
                self.memos = Memos.objects.filter(made_by=self.account_owner, keyword__icontains=self.keyword)
                self.context = {
                    'search':self.memos
                }
        else:
            if self.account_owner.user_id != session:
                self.memos = Memos.objects.filter(made_by=self.account_owner, disclose="public", subject__icontains=self.keyword).exclude(tab_name="TRASH")
                self.context = {
                    'search':self.memos
                }

            else:
                self.memos = Memos.objects.filter(made_by=self.account_owner, subject__icontains=self.keyword)
                self.context = {
                    'search':self.memos
                }
