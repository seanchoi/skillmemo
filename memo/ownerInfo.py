from memo.models import *
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
# owner contents information class
class Owner:
    def __init__(self, owner_id):    
        self.owner = Users.objects.get(user_id=owner_id)
        self.ownerMemos = Memos.objects.filter(made_by=self.owner).exclude(tab_name="TRASH")
        self.ownerPublicMemos = Memos.objects.filter(made_by=self.owner, disclose="public").exclude(tab_name="TRASH")

    def overTimePublicMemos(self):
        timePeriod = datetime.now() - timedelta(days=15)
        overMonthPublicMemos = Memos.objects.filter(made_by=self.owner,created_at__lt=timePeriod, disclose="public").exclude(tab_name="TRASH")
        return overMonthPublicMemos
    
    def overTimeMemos(self):
        timePeriod = datetime.now() - timedelta(days=15)
        overMonthPublicMemos = Memos.objects.filter(made_by=self.owner, created_at__lt=timePeriod)
        return overMonthPublicMemos

    def PublicCrumbs(self):
        allPublicCrumbs = []
        for memo in self.ownerPublicMemos:
            allPublicCrumbs.append(memo.keyword)
        sortedPublicCrumbs = list(set(allPublicCrumbs))
        return sortedPublicCrumbs

    def Crumbs(self):
        allCrumbs = []
        for memo in self.ownerMemos:
            allCrumbs.append(memo.keyword)
        sortedCrumbs = list(set(allCrumbs))
        return sortedCrumbs

    def YouTubeId(self, YouTubeUrl):
        video_id = ""
        if YouTubeUrl:
            for i in range(len(YouTubeUrl)):               
                if YouTubeUrl[i] == "=":
                    for s in range(i+1, len(YouTubeUrl)):
                        video_id = video_id + YouTubeUrl[s]                    
        return video_id