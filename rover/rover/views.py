from django.shortcuts import render
from rover.models import Profile,Stay

from django.contrib.auth.models import User
from pprint import pprint

def index(request):    
    
    
    profile_list = []
    
    profiles = Profile.objects.filter(type=2).order_by('-rank')
    for profile in profiles:
        total=0
        rating = 0
        
        stays = Stay.objects.filter(sitter=profile.user)
        
        for stay_count,stay in enumerate(stays):
            total += stay.rating
        if stay_count >0:
            rating = float(total / stay_count)
            
        profile_list.append({"image" : profile.image, "first_name" : profile.user.first_name, "rating" : rating, "text" : profile.text})
    
    
    context = {'profiles': profile_list,}
    
    return render(request, 'rover/index.html', context)


