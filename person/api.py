from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import Name, Address, EmailAddress, Phone
from .serializers import PersonSerializer, AddressSerializer, EmailAddressSerializer, PhoneSerializer


class PersonViewSet(ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (permissions.IsAuthenticated,)


class EmailAddressViewSet(ModelViewSet):
    queryset = EmailAddress.objects.all()
    serializer_class = EmailAddressSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PhoneViewSet(ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = (permissions.IsAuthenticated,)
