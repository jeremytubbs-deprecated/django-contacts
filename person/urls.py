from .api import PersonViewSet, AddressViewSet, EmailAddressViewSet, PhoneViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'emails', EmailAddressViewSet)
router.register(r'phones', PhoneViewSet)

urlpatterns = router.urls
