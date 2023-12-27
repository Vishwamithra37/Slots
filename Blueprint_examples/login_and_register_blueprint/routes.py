import config
from flask import Blueprint
from . import dbops

site = Blueprint("site", __name__)


@site.route("/", methods=["GET"])
def index():
    print(dbops.RPM)
    print(config.APPLES)
    return "Hello World!"
