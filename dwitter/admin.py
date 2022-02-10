# dwitter/admin.py

from django.contrib import admin
from django.contrib.auth.models import Group, User

# Remove fields the tutorial will not use from the Users
# Do not use insecure, password free users in production EVER
class UserAdmin(admin.ModelAdmin):
    model = User
    # only display the username field
    fields = ["username"]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
