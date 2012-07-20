from contacts.models import Contact
from django.contrib import admin

class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,  {'fields': ['name', 'age', 'email']}),
#            (None,  {'fields':['age']})
                ]
                                    

admin.site.register(Contact, ContactAdmin)
