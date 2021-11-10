from django.contrib import admin
from .models import Roll
from .models import User
from .models import Group,GroupDetails
from .models import Subject

# Register your models here.
admin.site.register(Roll)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(GroupDetails)
admin.site.register(Subject)