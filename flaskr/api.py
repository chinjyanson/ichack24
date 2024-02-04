from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import random

from modules.game import Levels, getplayer

api_bp = Blueprint('api', __name__,
                        template_folder='templates', url_prefix="/api")

@api_bp.route('/')
def index():
    return "nothing to see here"

@api_bp.route('/dbgprint')
def dbgprint():
    return {
        "assets" : [(a.__class__.__name__, a.value) for a in getplayer().assets.assets.values()],
        "income" : getplayer().income,
        "time": getplayer().time,
        "current_level": (getplayer().current_level.name, getplayer().current_level.value),
        "avg_happiness": getplayer().avg_happiness,
        "value":getplayer().assets.getTotalValue()
    }


@api_bp.route('/level')
def level():
    """Get life levels"""
    return  {i.name: i.value for i in Levels}

@api_bp.route('/nextmonth')
def nextmonth():
    """Get life levels"""
    return getplayer().execmonth()
    # return  {i.name: i.value for i in Levels}

@api_bp.route('/dbgsetsaving/<int:value>')
def setsaving(value):
    """Set saavingg levels"""
    getplayer().assets.increaseSavings(value=value)
    return "ok"

@api_bp.route('/dbgsetincome/<int:value>')
def setincome(value):
    """Set income levels"""
    getplayer().income = value
    return "ok"

@api_bp.route('/level/<float:level>')
def setlevel(level) -> tuple[bool, str]:
    """Set life levels, by value"""
    if (newlevel:=Levels(level)):
        getplayer().current_level = newlevel
        return "Success", 200
    return  "Invalid level", 500


@api_bp.route('/buy/<assetname>/<int:value>')
def buy(assetname, value):
    """Buy asset with value (in gbp)"""
    success, msg = getplayer().assets.buy(assetname, value)
    if not success:
        return  msg, 500
    return msg

@api_bp.route('/sell/<assetname>/<int:value>')
def sell(assetname, value):
    """Sell asset with value (in gbp)"""
    success, msg = getplayer().assets.sell(assetname, value)
    if not success:
        return  msg, 500
    return msg, 200

@api_bp.route('/getassets')
def getassets():
    """...."""
    return getplayer().assets.getValues()

@api_bp.route('/gettotal')
def gettotal():
    """...."""
    return {"value":getplayer().assets.getTotalValue()}

@api_bp.route('/getimage')
def getimage():
    """...."""
    return {"value":getplayer().assets.getTotalValue()}
