import requests
import json
from django.apps import apps
from django_menus.menu import MenuMixin, MenuItem


class DemoViewMixin:

    def package_button(self):
        a = apps.get_app_configs()
        dropdown = []
        button_text = ''
        for c in a:
            if hasattr(c, 'pypi'):
                if c.path.split('/')[-1] == self.__class__.__module__.split('.')[0]:
                    button_text = c.pypi
                    self.pypi_package = c.pypi
                else:
                    dropdown.append((c.pypi))
        return MenuItem(menu_display=button_text, dropdown=dropdown)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.menus['main_menu'].menu_items.insert(0, self.package_button())
        r = requests.get('https://pypi.org/pypi/{}/json'.format(self.pypi_package))
        pypi = json.loads(r.text)
        context['version'] = pypi['info']['version']
        context['version_img'] = 'https://badge.fury.io/py/{}.svg'.format(self.pypi_package)
        context['home_page'] = pypi['info']['home_page']
        return context
