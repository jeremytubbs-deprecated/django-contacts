from rest_framework import serializers
from .models import Name, Address, EmailAddress, Phone


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('street', 'city', 'state', 'postal_code', 'address_type', 'url')


class EmailAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailAddress
        fields = ('email', 'email_type', 'url')


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = ('phone', 'phone_type', 'url')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    addresses = AddressSerializer(read_only=True, many=True)
    emails = EmailAddressSerializer(read_only=True, many=True)
    phones = PhoneSerializer(read_only=True, many=True)

    class Meta:
        model = Name
        fields = ('first_name', 'last_name', 'note', 'phones', 'addresses', 'emails', 'url')
