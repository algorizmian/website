from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail', 'image')


admin.site.register(Project, ProjectAdmin)

