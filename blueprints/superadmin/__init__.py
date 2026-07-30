

from flask import Blueprint

superadmin_bp = Blueprint(
    "superadmin",
    __name__,
    url_prefix="/superadmin",
    template_folder="../../templates"
)

from . import routes