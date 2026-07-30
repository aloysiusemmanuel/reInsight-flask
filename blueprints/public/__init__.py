from flask import Blueprint

public_bp = Blueprint(
    "public",
    __name__,
    url_prefix="",
    template_folder="../../templates"
)

from . import routes
