from django.contrib import admin
from .models import Contact, Newsletter


class SubscribedNewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_on')


admin.site.register(Contact)
admin.site.register(Newsletter, SubscribedNewsletterAdmin)
