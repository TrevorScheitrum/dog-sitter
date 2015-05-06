from django.test import TestCase
from rover.models import Profile, Dog, Stay
from django.contrib.auth.models import User

from rover.utils import *
from datetime import datetime
import string


class util(TestCase):
    def test_cleaning_names(self):
        name="Mr. firstname las#*&^$t2name"
        name = remove_non_ascii_letters(name)
        self.assertEqual(name, 'Mrfirstnamelastname')
        
    def test_calculate_sitter_score(self):
        name=string.lowercase[:26]
        sitter_score = calculate_sitter_score(name)
        self.assertEqual(sitter_score, 5.0)
        
    def test_calculate_rating_score(self):
        owner = User.objects.create(username="owner1",first_name=" mr. first", last_name="last2")
        sitter = User.objects.create(username="sitter1",first_name=" mr. first", last_name="last2")
        sitterProfile = Profile.objects.create(user=sitter, type=2, image="http://google.com",text="this is my intro text",rank=4)
        
        
        dog1 = Dog.objects.create(name="dog1", owner=owner)
        dog2 = Dog.objects.create(name="dog2", owner=owner)
        stay1 = Stay.objects.create(sitter=sitter,profile=sitterProfile,rating=4, start_date=datetime.now(), end_date=datetime.now())
        stay_list = [stay1]
        print stay_list
        rating_score = calculate_rating_score(stay_list)
        self.assertEqual(rating_score, 4)
        
    def test_calculate_overall_sitter_rank(self):
        
        owner = User.objects.create(username="owner1",first_name=" mr. first", last_name="last2")
        sitter = User.objects.create(username="sitter1",first_name=" mr. first", last_name="last2")
        sitterProfile = Profile.objects.create(user=sitter, type=2, image="http://google.com",text="this is my intro text",rank=4)
        
        
        dog1 = Dog.objects.create(name="dog1", owner=owner)
        dog2 = Dog.objects.create(name="dog2", owner=owner)
        stay1 = Stay.objects.create(sitter=sitter,profile=sitterProfile,rating=4, start_date=datetime.now(), end_date=datetime.now())
        
        rating_score = calculate_rating_score([stay1])
        name=string.lowercase[:26]
        
        sitter_score = calculate_sitter_score(name)
        overall_score = calculate_overall_sitter_rank([stay1],sitter_score)
        
        stay_ratio = 1/10
        sitter_ratio = 9/10
        
        self.assertEqual(overall_score, float(rating_score)*float(stay_ratio) + float(sitter_score)*float(sitter_ratio))
        
        