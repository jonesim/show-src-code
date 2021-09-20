from django.apps import apps
from django.urls import path, include

from .modals import BaseSourceCodeModal

local_patterns = [
    path('modal/source_code/<str:slug>/', BaseSourceCodeModal.as_view(), name='source_code_modal'),
]

urlpatterns = [
    path('', include((local_patterns, 'show_src_code'))),
    # Load urls file from app if urls is setup in AppConfig
    *[path('', include((a.urls, ''),)) for a in apps.get_app_configs() if hasattr(a, 'urls')]
]
