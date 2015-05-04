from django.contrib import admin
from rover.models import Profile, Dog, Stay

admin_classes = [Profile,Dog,Stay]
admin.site.register(admin_classes)