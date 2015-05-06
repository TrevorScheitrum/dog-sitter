from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from rover.utils import *

class Dog(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User)
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
        return self.user.first_name

class Stay(models.Model):
    dogs = models.ManyToManyField(Dog)
    sitter = models.ForeignKey(User)
    profile = models.ForeignKey(Profile)
    CHOICES = [(i,i) for i in range(6)]
    rating = models.PositiveIntegerField(choices=CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    
    
    #Since the ranking algorithm is determined by each 'stay', update 
    #a users overall ratings as go
    def save(self, *args, **kwargs):
        super(Stay, self).save(*args, **kwargs)
        
        stay_objects = Stay.objects.filter(sitter_id=self.sitter_id)

        sitter_score = calculate_sitter_score(self.sitter.first_name)
        overall_sitter_rank = calculate_overall_sitter_rank(stay_objects,sitter_score)
        
        person_sitter = User.objects.get(pk=self.sitter.id)
        update_profile, created = Profile.objects.get_or_create(pk=person_sitter.profile.id)
        
        update_profile.rank = overall_sitter_rank
        update_profile.save()
    
    def __unicode__(self):
        return self.sitter.first_name +" "+ unicode(self.start_date) + "-" + unicode(self.end_date)



