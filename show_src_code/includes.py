from ajax_helpers.html_include import SourceBase, pip_version

version = pip_version('django-show-source-code')


class ShowSrcCode(SourceBase):
    static_path = 'show_src_code/'
    filename = 'highlightjs'
    js_path = ''
    css_path = ''


class DefaultInclude(ShowSrcCode):
    pass
