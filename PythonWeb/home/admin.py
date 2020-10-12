from django.contrib import admin
from .models import *
# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ['nameBooking', 'emailBooking', 'phoneBooking', 'checkInBooking', 'timeBooking']
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
admin.site.register(Booking, BookingAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(MasterChef, MasterChefAdmin)
admin.site.register(Blog, BlogAdmin)