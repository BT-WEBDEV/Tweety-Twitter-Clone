from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

# Create your models here.


User = settings.AUTH_USER_MODEL

class FollowerRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=220, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)

    '''
    Why is related name called "following" instead of "followers"
    project_obj = Projects.objects.first()
    project_obj.follwers.all() -> All users following this profile
    user.following.all() -> All user profiles I follow
    '''

# Signal Trigger Function - Once an account is made it will create a profile user. 
def user_did_save(sender, instance, created, *args, **kwargs):
    if created: 
        Profile.objects.get_or_create(user=instance)

post_save.connect(user_did_save, sender=User)

# Another example - after the user logs in -> verifty profile. 