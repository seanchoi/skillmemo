# from memo.acctSettings import *
# from memo.models import Users, TabColors

# class TabTheme:
#     def __init__(self, user_id, tab_theme):
#         self.account_owner = Users.objects.get(user_id=user_id)
#         self.tab_color = TabColors.objects.get(owner=self.account_owner)
#         if tab_theme == "spring":
#             self.account_owner.tab_theme = "spring"
#             self.account_owner.save()
#             self.tab_color.tcolor01 = "spring01"
#             self.tab_color.tcolor02 = "spring02"
#             self.tab_color.tcolor03 = "spring03"
#             self.tab_color.tcolor04 = "spring04"
#             self.tab_color.tcolor05 = "spring05"
#             self.tab_color.save()
#         elif tab_theme == "summer":
#             self.account_owner.tab_theme = "summer"
#             self.account_owner.save()
#             self.tab_color.tcolor01 = "summer01"
#             self.tab_color.tcolor02 = "summer02"
#             self.tab_color.tcolor03 = "summer03"
#             self.tab_color.tcolor04 = "summer04"
#             self.tab_color.tcolor05 = "summer05"
#             self.tab_color.save()
#         elif tab_theme == "autumn":
#             self.account_owner.tab_theme = "autumn"
#             self.account_owner.save()
#             self.tab_color.tcolor01 = "autumn01"
#             self.tab_color.tcolor02 = "autumn02"
#             self.tab_color.tcolor03 = "autumn03"
#             self.tab_color.tcolor04 = "autumn04"
#             self.tab_color.tcolor05 = "autumn05"            
#             self.tab_color.save()
#         elif tab_theme == "winter":
#             self.account_owner.tab_theme = "winter"
#             self.account_owner.save()
#             self.tab_color.tcolor01 = "winter01"
#             self.tab_color.tcolor02 = "winter02"
#             self.tab_color.tcolor03 = "winter03"
#             self.tab_color.tcolor04 = "winter04"
#             self.tab_color.tcolor05 = "winter05"
#             self.tab_color.save()
#         elif tab_theme == "study":
#             self.account_owner.tab_theme = "study"
#             self.account_owner.save()
#             self.tab_color.tcolor01 = "study01"
#             self.tab_color.tcolor02 = "study02"
#             self.tab_color.tcolor03 = "study03"
#             self.tab_color.tcolor04 = "study04"
#             self.tab_color.tcolor05 = "study05"
#             self.tab_color.save()