import json
import requests
from django.apps import AppConfig


class PypiAppConfig(AppConfig):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        r = requests.get('https://pypi.org/pypi/{}/json'.format(self.pypi))
        self.pypi_data = json.loads(r.text)


class SrcCodeConfig(AppConfig):
    name = 'show_src_code'
