from django.contrib import admin

# Register your models here.
from .models import Project, Tag, ProjectImage, UserProfile, UserProfileImage

class UserImageInline(admin.TabularInline):
    model = UserProfileImage
    extra = 1

class UserAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [UserImageInline]
    search_fields = ("name","description","linkedin","github")



class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title","link")
    inlines = [ProjectImageInline]
    search_fields = ("title","description")
    lister_filter = ("tags",)

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(UserProfile, UserAdmin)
admin.site.register(UserProfileImage)