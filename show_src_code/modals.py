import django_modals.modals as modals
from django.utils.safestring import mark_safe
from django.utils.module_loading import import_string
from django_modals.modals import Modal
from .source_code import template_source, html_code


class BaseSourceCodeModal(Modal):
    size = 'xl'
    modal_title = 'Source Code'
    code = {'template_src': 'crud'}

    def modal_content(self):
        if 'pk' in self.slug:
            # Try to get callable from dictionary
            function_class = self.code.get(self.slug['pk'])
            if callable(function_class):
                code = html_code(function_class)
            else:
                a = import_string(self.kwargs['pk'])
                code = html_code(a)
        if 'template' in self.slug:
            if 'templateSection' in self.slug:
                code += template_source(self.slug['template'].replace(':', '/'), self.slug['templateSection'])
            else:
                code += template_source(self.slug['template'].replace(':', '/'))
        return code

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['script'] = mark_safe('hljs.highlightAll();')
        return context


class CodeMixin:

    def get_context_data(self, **kwargs):
        # noinspection PyUnresolvedReferences
        context = super().get_context_data(**kwargs)
        context['footer'] = mark_safe('''<div class="p-1" style="text-align:right;background-color:#efefef">
            <button class='btn btn-sm btn-outline-secondary' onclick='django_modal.send_inputs({"button": "code"})'>
            <i class="fab fa-python"></i> Source Code</button></div>''')
        return context

    def button_code(self, **_kwargs):
        code = ''
        try:
            if hasattr(self, 'form_class'):
                code = html_code(self.form_class)
        except OSError:
            pass
        if isinstance(self, TemplateModal):
            code += template_source(self.modal_template)
        code += html_code(self.__class__)
        # noinspection PyUnresolvedReferences
        return self.message(message=code, size='xl', title='Source Code', script=mark_safe('hljs.highlightAll();'))


class FormModal(CodeMixin, modals.FormModal):
    pass


class ModelFormModal(CodeMixin, modals.ModelFormModal):
    pass


class MultiFormModal(CodeMixin, modals.MultiFormModal):
    pass


class BaseModal(CodeMixin, modals.BaseModal):
    pass


class Modal(CodeMixin, modals.Modal):
    pass


class TemplateModal(CodeMixin, modals.TemplateModal):
    pass
