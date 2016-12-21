from django.contrib import admin
from person.models import Name, Address, EmailAddress, Phone

class AddressInline(admin.TabularInline):
    model = Address
    extra = 1


class EmailInline(admin.TabularInline):
    model = EmailAddress
    extra = 1


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline,
        EmailInline,
        PhoneInline,
    ]
    search_fields = [
        'first_name',
        'last_name',
    ]


admin.site.register(Name, PersonAdmin)
