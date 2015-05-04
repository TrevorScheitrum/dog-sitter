# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import csv
from rover.models import Profile, Dog, Stay
from django.contrib.auth.models import User
from rover.utils import *



def createDataModel(row):
    rating = row[0]
    sitter_image = row[1]
    end_date = row[2]
    text = row[3]
    owner_image = row[4]
    dogs = row[5]
    sitter = row[6]
    owner = row[7]
    start_date = row[8]
    
    sitter_id = sitter_image[sitter_image.index("=")+1:]
    owner_id = owner_image[owner_image.index("=")+1:]
    
    sitterScore = calculateSitterScore(sitter)
    
    if not User.objects.filter(pk=owner_id).exists():
        owner, ownerCreated = User.objects.get_or_create(pk=owner_id, username=owner_id, first_name=str.split(owner)[0])
        owner.profile = Profile(type=1, image=owner_image)
        owner.profile.save()
    
    if not User.objects.filter(pk=sitter_id).exists():
        sitter, sitterCreated = User.objects.get_or_create(pk=sitter_id, username=sitter_id, first_name=str.split(sitter)[0])
        sitter.profile = Profile(type=2,text=text, rank=sitterScore, image=sitter_image)
        sitter.profile.save()
             
    sitter = User.objects.get(pk=sitter_id)
    owner = User.objects.get(pk=owner_id)
    
    dogs = dogs.split('|')
    dogList = []
    for dog in dogs:
       newDog = Dog(name=dog, owner=owner) 
       newDog.save()
       dogList.append(newDog)
       
    newStay = Stay(sitter_id=sitter_id,rating=rating,start_date=start_date,end_date=end_date)
    newStay.save()
    newStay.dogs.add(*dogList)
    newStay.save()


def import_data(apps, schema_editor):
    with open('../reviews.csv', 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter=b',')
        datareader.next()
        for row in datareader:
            createDataModel(row)


class Migration(migrations.Migration):

    dependencies = [
        ('rover', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_data),
    ]
