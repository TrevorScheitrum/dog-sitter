from django.shortcuts import render
from rover.models import Profile

def index(request):
    
    profiles = Profile.objects.filter(type=2).order_by('-rank')
    
    context = {'profiles': profiles,}
    
    return render(request, 'rover/index.html', context)


