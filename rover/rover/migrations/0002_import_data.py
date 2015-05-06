# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import csv
from rover.models import Profile, Dog, Stay
from django.contrib.auth.models import User
from rover.utils import *



def create_data_model(row):
    rating = int(row[0])
    sitter_image = row[1]
    end_date = row[2]
    text = row[3]
    owner_image = row[4]
    dogs = row[5]
    sitter = row[6]
    owner = row[7]
    start_date = row[8]
    
    
    # Get unique user id from salvaged image urls
    sitter_id = sitter_image[sitter_image.index("=")+1:]
    owner_id = owner_image[owner_image.index("=")+1:]
    
    sitter_score = calculate_sitter_score(sitter)
    
    
    #create an owner if it doesn't exist
    if not User.objects.filter(pk=owner_id).exists():
        owner, owner_created = User.objects.get_or_create(pk=owner_id, username=owner_id, first_name=owner)
        owner.profile = Profile(type=1, image=owner_image)
        owner.profile.save()
    
    #create a sitter if it doesn't exist
    if not User.objects.filter(pk=sitter_id).exists():
        sitter, sitter_created = User.objects.get_or_create(pk=sitter_id, username=sitter_id, first_name=sitter)
        sitter.profile = Profile(type=2,text=text, rank=sitter_score, image=sitter_image)
        sitter.profile.save()
    
    sitter = User.objects.get(pk=sitter_id)
    owner = User.objects.get(pk=owner_id)
    
    
    #Get multiple dog name from one line
    dogs = dogs.split('|')
    dog_list = []
    
    #Create new dogs for each dogname salvaged
    for dog in dogs:
       new_dog = Dog(name=dog, owner=owner) 
       new_dog.save()
       dog_list.append(new_dog)
    
    #Create 'stays' for each dog
    newStay = Stay(sitter_id=sitter_id,profile=sitter.profile,rating=rating,start_date=start_date,end_date=end_date)
    newStay.save()
    newStay.dogs.add(*dog_list)
    newStay.save()


def import_data(apps, schema_editor):
    with open('../reviews.csv', 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter=b',')
        datareader.next()
        for row in datareader:
            create_data_model(row)


class Migration(migrations.Migration):

    dependencies = [
        ('rover', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_data),
    ]
