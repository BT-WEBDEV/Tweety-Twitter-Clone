import random
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class TweetLike(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Tweet (models.Model):
    # id = models.AutoField(primary_key=True) DEFAULT
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign Key = one user can have many tweets (instead of many tweets can have many users)
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike) # Store indivdual users into likes. Many to Many = 1 Tweet could have many users. Many users can have many tweets 
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    #def __str__(self): 
        #return self.content

    class Meta: 
        ordering = ['-id']

    @property
    def is_retweet(self): 
        return self.parent != None

    def serialize(self): 
        '''
        Feel Free to Delete
        '''
        return {
            "id": self.id, 
            "content": self.content, 
            "likes": random.randint(0,200)
        }

    