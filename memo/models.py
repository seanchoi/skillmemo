from django.db import models
import re
from django.utils import timezone

now = timezone.now()

class userManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name must be at least 2 characters"        
        if not postData['first_name'].isalpha():
            errors['first_name_letterOnly'] ="Name must be alphabet characters only"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name must be at least 2 characters" 
        if not postData['last_name'].isalpha():
            errors['last_name_letterOnly'] ="Name must be alphabet characters only"
        if len(postData['user_id']) < 6:
            errors['user_id'] = "user ID, at least 6 characters"
        user_id = Users.objects.filter(user_id=postData['user_id'])
        if len(user_id):
            if postData['user_id'] == user_id[0].user_id:
                errors['user_id'] = "user ID is not available"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    
            errors['email'] = ("Invalid email address format!")
        email = Users.objects.filter(email=postData['email'])
        if len(email):
            if postData['email'] == email[0].email:
                errors['duplicate_email'] = "The email is already registered"
        if len(postData['password']) < 8:
            errors['password'] = "Passwords, at least 8 chracters"
        if postData['password'] != postData['confirm']:
            errors['confirm'] = "Password does not match"

        return errors

class dmManager(models.Manager):
    def validator(self, postData):
        errors = {}
        users = Users.objects.filter(user_id=postData['to'])
        if not len(users):
            errors['no_user_found'] = "No User Found"
        return errors    

class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255, null=True)
    brand_desc = models.CharField(max_length=255, null=True)
    profile_pic = models.ImageField(upload_to="profile_pic/%Y/%m/%d", blank=True, null=True)    
    tab01 = models.CharField(max_length=50, default="Tab #1")
    tab02 = models.CharField(max_length=50, default="Tab #2")
    tab03 = models.CharField(max_length=50, default="Tab #3")
    tab04 = models.CharField(max_length=50, default="Tab #4")
    tab05 = models.CharField(max_length=50, default="Tab #5")
    tab06 = models.CharField(max_length=50, default="TRASH")
    tab_view = models.CharField(max_length=50, default="on")
    tab_theme = models.CharField(max_length=50, default="study")
    view_mode = models.CharField(max_length=50, default="social media mode")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Memos(models.Model):
    made_by = models.ForeignKey(Users,related_name='memo', on_delete=models.CASCADE)
    users = models.ManyToManyField(Users, related_name='saved')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    content_code = models.TextField(null=True)
    language = models.TextField(max_length=30, null=True)
    desc = models.TextField(null=True)
    image01 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)
    image02 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)
    image03 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)
    image04 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)
    style_first = models.CharField(max_length=255, null=True)
    image05 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)
    image06 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)
    image07 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)
    image08 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)
    style_second = models.CharField(max_length=255, null=True)
    image09 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)
    image10 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)
    style_third = models.CharField(max_length=255, null=True)
    subject_2nd = models.CharField(max_length=255,null=True)
    content_2nd = models.TextField(null=True)
    desc_2nd = models.TextField(null=True)
    subject_3rd = models.CharField(max_length=255,null=True)
    content_3rd = models.TextField(null=True)
    desc_3rd = models.TextField(null=True)
    video01 = models.TextField(null=True)
    video02 = models.TextField(null=True)
    video03 = models.TextField(null=True)
    keyword = models.CharField(max_length=20, null=True)
    tab_name = models.CharField(max_length=20, null=True)
    disclose = models.CharField(max_length=20, default="public")    
    comment_on = models.CharField(max_length=20) 
    password = models.CharField(max_length=16, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image01.delete()
        self.image02.delete()
        self.image03.delete()
        self.image04.delete()
        self.image05.delete()
        self.image06.delete()
        self.image07.delete()
        self.image08.delete()
        self.image09.delete()
        self.image10.delete()
        super().delete(*args, **kwargs)

class Photos(models.Model):
    user = models.CharField(max_length=255, blank=True)
    files = models.FileField(upload_to="memo_images_first_section/", blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Photos02(models.Model):
    user = models.CharField(max_length=255, blank=True)
    files = models.FileField(upload_to="memo_images_second_section/", blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Photos03(models.Model):
    user = models.CharField(max_length=255, blank=True)
    files = models.FileField(upload_to="memo_images_third_section/", blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Comments(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    reply_by_profile_pic = models.CharField(max_length=255, null=True)
    reply_by_dashboard = models.CharField(max_length=255, null=True)
    reply_to = models.ForeignKey(Memos, related_name='comment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class DMs(models.Model):
    to = models.ForeignKey(Users, related_name="dm", on_delete=models.CASCADE, null=True)
    sent_by = models.ForeignKey(Users, related_name="dm_sent_by", on_delete=models.CASCADE, null=True)
    to_user_id = models.CharField(max_length=255, null=True)
    from_user_id = models.CharField(max_length=255, null=True)
    dm_msg = models.TextField(null=True)
    if_to_checked = models.CharField(max_length=5, default="no")
    if_to_reply_checked = models.CharField(max_length=5, default="no")
    if_from_reply_checked = models.CharField(max_length=5, default="yes")  
    created_at = models.DateTimeField(auto_now_add=True)
    objects = dmManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
class DmReply(models.Model):
    reply_for = models.ForeignKey(DMs, related_name="dm_reply", on_delete=models.CASCADE)
    parent_dm_id = models.CharField(max_length=255)
    reply_user_id = models.CharField(max_length=255)
    reply_name = models.CharField(max_length=255)
    reply_msg = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)