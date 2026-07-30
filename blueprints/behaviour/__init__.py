from flask import Blueprint

behaviour_bp = Blueprint(
    "behaviour",
    __name__,
    url_prefix="/behaviour",
    template_folder="../../templates"
    
)

from . import routes