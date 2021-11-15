from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Roll
from .models import User
from .models import Group,GroupDetails
from .models import Subject


#ecxcel用   
class    UserResource(resources.ModelResource):
    class Meta:
        model = User
        import_id_fields = ["userid"]
# 管理
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource

# Register your models here.
admin.site.register(Roll)
admin.site.register(User,UserAdmin)
admin.site.register(Group)
admin.site.register(GroupDetails)
admin.site.register(Subject)