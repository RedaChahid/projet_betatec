from django.urls import path
from .views import Home,Accueil,Services,projets,propos,Contact
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('Accueil/',Accueil.as_view(),name='Vehi'),
    path('Services/',Services.as_view(),name='Immo'),
    path('projets/',projets.as_view(),name='Info'),
    path('propos/',propos.as_view(),name='Lois'),
    path('Contact/',Contact.as_view(), name='Cont'),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
