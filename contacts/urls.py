from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ensure_csrf_cookie(TemplateView.as_view(template_name="home.html"))),
    url(r'^contacts/', include('person.urls')),
]
