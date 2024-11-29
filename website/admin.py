from django.contrib import admin
from .models import Post, Person, Command, Questions

class CommandAdmin(admin.ModelAdmin):
    filter_horizontal = ('members',)  

admin.site.register(Post)
admin.site.register(Person)
admin.site.register(Command, CommandAdmin)
admin.site.register(Questions)
