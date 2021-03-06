########################################
# Jinja template handlers
########################################

import os

import jinja2

lookup = None
cache = {}


def get_template_lookup(directories):
    return jinja2.Environment(loader=jinja2.FileSystemLoader(
        directories,
        encoding='utf-8',
        ))


def render_template(template_name, output_name, context, global_context):
    template = lookup.get_template(template_name)
    local_context = {}
    #add template name to context
    local_context["template_name"] = template_name
    local_context.update(global_context)
    local_context.update(context)
    output = template.render(**local_context)
    if output_name is not None:
        try:
            os.makedirs(os.path.dirname(output_name))
        except:
            pass
        with open(output_name, 'w+') as output:
            output.write(output.encode('utf8'))
    return output


def template_deps(template_name):
    return []
