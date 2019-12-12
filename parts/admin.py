from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Client, Team
from .models import Attendance, Instructor
from .models import Applications


class MembershipInline(admin.TabularInline):
    model = Team.client.through


class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'card_id', 'birth_date', 'phone_number', 'pass_type', 'sub_status']
    list_filter = ['pass_type', 'sub_status']
    search_fields = ['first_name', 'last_name']
    readonly_fields = ['image_tag']
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'card_id', 'birth_date', 'phone_number', 'image_tag')
        }),
        ('Subscription', {
            'fields': ('pass_type', 'sub_months','sub_status', 'sub_initiated', 'sub_terminated', )
        }),
    )
    inlines = [MembershipInline]


class ClientInline(admin.TabularInline):
    model = Client


class InstructorAdmin(admin.ModelAdmin):
    list_display = ['trainer_name', 'phone_number']
    readonly_fields = ['image_tag']

    def trainer_name(self, obj):
        name = '{}  {}'.format(obj.first_name, obj.last_name)
        return name


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'date_attended']
    list_filter = ['date_attended', 'client']
    autocomplete_fields = ['client']


    def client_name(self, obj):
        name = '{}  {}'.format(obj.client.first_name, obj.client.last_name)
        return name

    client_name.short_description = 'Name'

class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'members', 'instructor', 'info', 'date']

    def instructor(self, obj):
        return obj.instructor

    def members(self, obj):
        x = "<br>".join([str(s.first_name) + ' ' + str(s.last_name) for s in obj.client.all()])
        return mark_safe(x)
    inlines = [MembershipInline]


class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'processed', 'message']
    list_filter = ['processed']


admin.site.register(Client, ClientAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Applications, ApplicationsAdmin)
admin.site.register(Attendance, AttendanceAdmin)
