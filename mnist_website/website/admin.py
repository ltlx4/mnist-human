from django.contrib import admin
from .models import User, UserImage


class UserImageAdmin(admin.StackedInline):
    model = UserImage

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated', 'number_of_guesses')
    inlines = [UserImageAdmin]
 
    class Meta:
       model = User

    def number_of_guesses(UserImage, obj):
        return obj.userimage_set.count()
 
@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    pass
