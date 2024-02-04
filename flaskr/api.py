from flask import Blueprint, render_template, abort, session
from jinja2 import TemplateNotFound
import random

from modules.game import Levels, Player, players

api_bp = Blueprint('api', __name__,
                        template_folder='templates', url_prefix="/api")

@api_bp.route('/')
def index():
    return "nothing to see here"

@api_bp.route('/dbgprint')
def dbgprint():
    return {
        "assets" : [(a.__class__.__name__, a.value) for a in players[session["id"]].assets.assets.values()],
        "income" : players[session["id"]].income,
        "time": players[session["id"]].time,
        "current_level": (players[session["id"]].current_level.name, players[session["id"]].current_level.value),
        "avg_happiness": players[session["id"]].avg_happiness,
        "value":players[session["id"]].assets.getTotalValue()
    }


@api_bp.route('/level')
def level():
    """Get life levels"""
    return  {i.name: i.value for i in Levels}

@api_bp.route('/nextmonth')
def nextmonth():
    """Get life levels"""
    return players[session["id"]].execmonth()
    # return  {i.name: i.value for i in Levels}

@api_bp.route('/dbgsetsaving/<int:value>')
def setsaving(value):
    """Set saavingg levels"""
    players[session["id"]].assets.increaseSavings(value=value)
    return "ok"

@api_bp.route('/dbgsetincome/<int:value>')
def setincome(value):
    """Set income levels"""
    players[session["id"]].income = value
    return "ok"

@api_bp.route('/level/<float:level>')
def setlevel(level) -> tuple[bool, str]:
    """Set life levels, by value"""
    if (newlevel:=Levels(level)):
        players[session["id"]].current_level = newlevel
        return "Success", 200
    return  "Invalid level", 500


@api_bp.route('/buy/<assetname>/<int:value>')
def buy(assetname, value):
    """Buy asset with value (in gbp)"""
    success, msg = players[session["id"]].assets.buy(assetname, value)
    if not success:
        return  msg, 500
    return msg

@api_bp.route('/sell/<assetname>/<int:value>')
def sell(assetname, value):
    """Sell asset with value (in gbp)"""
    success, msg = players[session["id"]].assets.sell(assetname, value)
    if not success:
        return  msg, 500
    return msg, 200

@api_bp.route('/getassets')
def getassets():
    """...."""
    return players[session["id"]].assets.getValues()

@api_bp.route('/gettotal')
def gettotal():
    """...."""
    return {"value":players[session["id"]].assets.getTotalValue()}

@api_bp.route('/getimage')
def getimage():
    """...."""
    return {"value":players[session["id"]].assets.getTotalValue()}
