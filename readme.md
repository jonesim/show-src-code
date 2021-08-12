[![PyPI version](https://badge.fury.io/py/django-show-source-code.svg)](https://badge.fury.io/py/django-show-source-code)

Add to installed apps

    'crispy_forms',
    'ajax_helpers',
    'django_modals',
    'show_src_code',

    
Add to template

    {% load static src_code %}
    {% highlightjs_includes %}
    <script src="{% static 'ajax_helpers/ajax_helpers.js' %}"></script>
    <link href="{% static 'ajax_helpers/ajax_helpers.css' %}" rel="stylesheet"/>    
    <script src="{% static 'django_modals/js/modals.js' %}"></script>
    <link rel="stylesheet" type="text/css" href="{% static 'django_modals/css/modals.css' %}"/>



Create subclass of BaseSourceCodeModal


    from show_src_code.modals import BaseSourceCodeModal
    
    class SourceCodeModal(BaseSourceCodeModal):
        code = {
            'code_identifier', Function or Class to display
        }
        
Add to urls

    path('source_code/<str:slug>', views.SourceCodeModal.as_view(), name='source_code')
   
In template

    {% load src_code%}   
    {% show_src_code 'source_code' 'code:id' %}
