from flask import Blueprint

teacher_dash_bp = Blueprint(
    "teacher_dashboard",
    __name__,
    url_prefix="/teacher-dashboard",
    template_folder="../../templates"
)

from . import routes