from flask import Blueprint

classrooms_bp = Blueprint(
    "classrooms",
    __name__,
    url_prefix="/classrooms",
    template_folder="../../templates"
)

from . import routes