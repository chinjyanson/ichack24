from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


api_bp = Blueprint('api', __name__,
                        template_folder='templates', url_prefix="/api")

@api_bp.route('/')
def index():
    return "nothing to see here"


@api_bp.route('/level')
def level():
    """Get life levels"""
    return {1:1000, 2:2000, 3:3000}

@api_bp.route('/level/<int:level>')
def setlevel(level):
    """Set life levels"""
    return "nothing to see here"


@api_bp.route('/buy/<assetname>/<int:value>')
def buy(name, value):
    """Buy asset with value (in pence)"""
    return "nothing to see here"

@api_bp.route('/sell/<assetname>/<int:value>')
def buy(name, value):
    """Sell asset with value (in pence)"""
    return "nothing to see here"
