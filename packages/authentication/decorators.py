"""
=========================================================
Authentication Decorators
=========================================================

Role-based access decorators for the reInsight
SaaS platform.
"""

from functools import wraps

from flask import (
    flash,
    redirect,
    url_for, abort
)

from flask_login import (
    current_user,
    login_required
)

from .utils import get_dashboard_url


# ==========================================================
# SUPER ADMIN REQUIRED
# ==========================================================

def superadmin_required(view):

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        if not current_user.is_authenticated:
            return redirect(
                url_for("superadmin.login")
            )

        if not current_user.is_super_admin:
            abort(403)

        return view(*args, **kwargs)

    return wrapped_view


# ==========================================================
# SCHOOL ADMIN REQUIRED
# ==========================================================

def school_admin_required(view):
    """
    Allows access only to School Administrators.
    """

    @wraps(view)
    @login_required
    def wrapped_view(*args, **kwargs):

        if not current_user.is_school_admin:
            flash(
                "You do not have permission to access this page.",
                "danger"
            )
            return redirect(get_dashboard_url(current_user))

        return view(*args, **kwargs)

    return wrapped_view


# ==========================================================
# TEACHER REQUIRED
# ==========================================================

def teacher_required(view):
    """
    Allows access only to Teachers.
    """

    @wraps(view)
    @login_required
    def wrapped_view(*args, **kwargs):

        if not current_user.is_teacher:
            flash(
                "You do not have permission to access this page.",
                "danger"
            )
            return redirect(get_dashboard_url(current_user))

        return view(*args, **kwargs)

    return wrapped_view


# ==========================================================
# PARENT REQUIRED
# ==========================================================

def parent_required(view):
    """
    Allows access only to Parents.
    """

    @wraps(view)
    @login_required
    def wrapped_view(*args, **kwargs):

        if not current_user.is_parent:
            flash(
                "You do not have permission to access this page.",
                "danger"
            )
            return redirect(get_dashboard_url(current_user))

        return view(*args, **kwargs)

    return wrapped_view