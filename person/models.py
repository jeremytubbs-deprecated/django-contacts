from django.db import models

class Name(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = ("Person")
        verbose_name_plural = ("People")


class Address(models.Model):
    ADDRESS_TYPES = (
        ('HOME', 'home'),
        ('WORK', 'work'),
        ('OTHER', 'other'),
    )
    street = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    postal_code = models.CharField(max_length=16, blank=True, null=True)
    address_type = models.CharField(max_length=5, choices=ADDRESS_TYPES)
    name = models.ForeignKey(Name, on_delete=models.CASCADE, related_name="addresses")


class EmailAddress(models.Model):
    EMAIL_TYPES = (
        ('HOME', 'home'),
        ('WORK', 'work'),
        ('OTHER', 'other'),
    )
    email = models.EmailField(max_length=200, blank=True, null=True)
    email_type = models.CharField(max_length=5, choices=EMAIL_TYPES)
    name = models.ForeignKey(Name, on_delete=models.CASCADE, related_name="emails")


class Phone(models.Model):
    PHONE_TYPES = (
        ('MOBILE', 'mobile'),
        ('HOME', 'home'),
        ('WORK', 'work'),
        ('HOME_FAX', 'home fax'),
        ('WORK_FAX', 'work fax'),
        ('OTHER_FAX', 'other fax'),
        ('PAGER', 'pager'),
        ('OTHER', 'other'),
    )
    phone = models.CharField(max_length=50, blank=True, null=True)
    phone_type = models.CharField(max_length=9, choices=PHONE_TYPES)
    name = models.ForeignKey(Name, on_delete=models.CASCADE, related_name="phones")
