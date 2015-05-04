from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from rover.utils import *

class Dog(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.name

class Stay(models.Model):
    dogs = models.ManyToManyField(Dog)
    sitter = models.ForeignKey(User)
    CHOICES = [(i,i) for i in range(5)]
    rating = models.PositiveIntegerField(choices=CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    
    
    
    def save(self, *args, **kwargs):
        super(Stay, self).save(*args, **kwargs)
        
        stayObjects = Stay.objects.filter(sitter_id=self.sitter_id)

        sitterScore = calculateSitterScore(self.sitter.username)
        overallSitterRank = calculateOverallSitterRank(stayObjects,sitterScore)
            
        personSitter = User.objects.get(pk=self.sitter.id)
        updateProfile, created = Profile.objects.get_or_create(pk=personSitter.profile.id)
        
        updateProfile.rank = overallSitterRank
        updateProfile.save()
    
    def __unicode__(self):
        return self.sitter.username + unicode(self.start_date) + " - " + unicode(self.end_date)


class Profile(models.Model):
    user = models.OneToOneField(User,null=True)
    
    CHOICES = (
        (1, 'Owner'),
        (2, 'Sitter'),
        (3, 'Both'),
    )
    type = models.IntegerField(choices=CHOICES)
    
    image = models.URLField(null=True)
    text = models.TextField(null=True)
    rank = models.FloatField(null=True)
    
    
    def __unicode__(self):
        return self.user.username
