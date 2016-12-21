from django.contrib import admin
from person.models import Name, Address, EmailAddress, Phone

class AddressInline(admin.TabularInline):
    model = Address
    max_num = 1


class EmailInline(admin.TabularInline):
    model = EmailAddress
    max_num = 1


class PhoneInline(admin.TabularInline):
    model = Phone
    max_num = 1


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline,
        EmailInline,
        PhoneInline,
    ]


admin.site.register(Name, PersonAdmin)
