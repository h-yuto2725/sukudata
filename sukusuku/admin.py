from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Roll
from .models import User
from .models import Group,GroupDetails
#from .models import Subject
from .models import Class,ClassDetails
from .models import Timetable

  
class    UserResource(resources.ModelResource):
    class Meta:
        model = User
        import_id_fields = ["userid"]

class    TimetableResource(resources.ModelResource):
    class Meta:
        model = Timetable

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource

class TimetableAdmin(ImportExportModelAdmin):
    resource_class = TimetableResource

# Register your models here.
admin.site.register(Roll)
admin.site.register(User,UserAdmin)
admin.site.register(Group)
admin.site.register(GroupDetails)
#admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(ClassDetails)
admin.site.register(Timetable,TimetableAdmin)