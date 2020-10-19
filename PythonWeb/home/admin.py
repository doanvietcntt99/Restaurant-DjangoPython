from django.contrib import admin
from .models import *
# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ['nameBooking', 'emailBooking', 'phoneBooking', 'checkInBooking', 'timeBooking', 'numberOfGuest']
    list_filter = ['checkInBooking']
    search_fields = ['phoneBooking']
class FoodAdmin (admin.ModelAdmin):
    list_display = ['nameFood','ingredientFood','payFood','avatarFood','nameTypeFood']
    list_filter = ['nameTypeFood']
    search_fields = ['nameFood']
class MasterChefAdmin(admin.ModelAdmin):
    list_display = ['nameChef','positionChef','selfIntroduceChef','avatarChef']
class BlogAdmin(admin.ModelAdmin):
    list_display = ['nameBlog','posterBlog','titleBlog','contentBlog', 'avatarBlog', 'timePost','updatedPost']
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','author','body','date']
    search_fields = ['author']
    list_filter = ['post']
class TypeFoodAdmin(admin.ModelAdmin):
    list_display = ['nameTypeFood']
    search_fields = ['nameTypeFood']
class UserAdmin(admin.ModelAdmin):
    list_display = ['usernameUser','fullnameUser','dobUser','emailUser','addressUSer','phoneUser','avatarUser','statusUser']
    search_fields = ['fullnameUser']
    list_filter = ['statusUser']
admin.site.register(Booking, BookingAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(MasterChef, MasterChefAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(TypeFood, TypeFoodAdmin)
admin.site.register(User, UserAdmin)
