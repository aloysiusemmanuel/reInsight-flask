from flask import Blueprint

parents_bp = Blueprint(
    "parents",
    __name__,
    url_prefix="/parents",
    template_folder="../../templates"
)

from . import routes