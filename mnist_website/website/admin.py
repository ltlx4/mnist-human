from django.contrib import admin
from .models import User, UserImage

class UserImageAdmin(admin.StackedInline):
    model = UserImage

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [UserImageAdmin]
 
    class Meta:
       model = User
 
@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    pass