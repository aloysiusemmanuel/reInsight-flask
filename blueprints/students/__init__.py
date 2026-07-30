from flask import Blueprint

students_bp = Blueprint(
    "students",
    __name__,
    url_prefix="/students",
    template_folder="../../templates"
)

from . import routes