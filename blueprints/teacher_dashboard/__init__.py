from flask import Blueprint

teacher_bp = Blueprint(
    "teacher-dashboard",
    __name__,
    url_prefix="/teacher-dashboard",
    template_folder="../../templates"
)

from . import routes