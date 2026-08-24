"""
=========================================================
Authentication Blueprint
=========================================================

Blueprint:
    auth_bp

Routes:
    /auth/login
    /auth/logout
    /auth/forgot-password
    /auth/reset-password
    /auth/change-password
"""



from flask import Blueprint

# =========================================================
# AUTHENTICATION BLUEPRINT
# =========================================================

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
    template_folder="../../templates/auth"
)

from . import routes
from . import loaders
