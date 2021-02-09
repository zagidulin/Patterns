from jinja2 import Template
import os


def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param kwargs: параметры для передачи в шаблон
    """
    template_path = os.path.join(folder, template_name)
    with open(template_path, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)
