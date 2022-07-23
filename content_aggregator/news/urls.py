from django.urls import path

from .views import HomePage
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", HomePage.as_view(), name="homepage"),
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
