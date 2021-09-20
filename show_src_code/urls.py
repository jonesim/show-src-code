from django.apps import apps
from django.urls import path, include

from .modals import BaseSourceCodeModal

app_name = 'show_src_code'
urlpatterns = [
    path('modal/source_code/<str:slug>/', BaseSourceCodeModal.as_view(), name='source_code_modal'),
    # Load urls file from app if urls is setup in AppConfig
    *[path('', include(a.urls)) for a in apps.get_app_configs() if hasattr(a, 'urls')]
]
