from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

template_folder = 'gui'

index_page = Blueprint('index_page', 'index_page', template_folder=template_folder)


@index_page.route('/')
def get_index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
