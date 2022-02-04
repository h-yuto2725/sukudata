from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Role
from .models import User
from .models import Group
from .models import GroupDetails
#from .models import Subject
from .models import Class, ClassDetails
from .models import Timetable, Schedule, GroupSchedule
from .models import Event, Todo
from .models import Thread, Comment


class RoleResource(resources.ModelResource):
    class Meta:
        model = Role
        import_id_fields = ["roleid"]


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        import_id_fields = ["userid"]


class GroupResource(resources.ModelResource):
    class Meta:
        model = Group
        import_id_fields = ["groupid"]


class GroupDetailsResource(resources.ModelResource):
    class Meta:
        model = GroupDetails


class ClassResource(resources.ModelResource):
    class Meta:
        model = Class
        import_id_fields = ["classid"]


class ClassDetailsResource(resources.ModelResource):
    class Meta:
        model = ClassDetails


class TimetableResource(resources.ModelResource):
    class Meta:
        model = Timetable


class ScheduleResource(resources.ModelResource):
    class Meta:
        model = Schedule


class GroupScheduleResource(resources.ModelResource):
    class Meta:
        model = GroupSchedule


class EventResource(resources.ModelResource):
    class Meta:
        model = Event


class TodoResource(resources.ModelResource):
    class Meta:
        model = Todo


class ThreadResource(resources.ModelResource):
    class Meta:
        model = Thread
        import_id_fields = ["threadid"]


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment


class RoleAdmin(ImportExportModelAdmin):
    resource_class = RoleResource


class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource


class GroupAdmin(ImportExportModelAdmin):
    resource_class = GroupResource


class GroupDetailsAdmin(ImportExportModelAdmin):
    resource_class = GroupDetailsResource


class ClassAdmin(ImportExportModelAdmin):
    resource_class = ClassResource


class ClassDetailsAdmin(ImportExportModelAdmin):
    resource_class = ClassDetailsResource


class TimetableAdmin(ImportExportModelAdmin):
    resource_class = TimetableResource


class ScheduleAdmin(ImportExportModelAdmin):
    resource_class = ScheduleResource


class GroupScheduleAdmin(ImportExportModelAdmin):
    resource_class = GroupScheduleResource


class EventAdmin(ImportExportModelAdmin):
    resource_class = EventResource


class TodoAdmin(ImportExportModelAdmin):
    resource_class = TodoResource


class ThreadAdmin(ImportExportModelAdmin):
    resource_class = ThreadResource


class CommentAdmin(ImportExportModelAdmin):
    resource_class = CommentResource


# Register your models here.
admin.site.register(Role, RoleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(GroupDetails, GroupDetailsAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(ClassDetails, ClassDetailsAdmin)
admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(GroupSchedule, GroupScheduleAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)
