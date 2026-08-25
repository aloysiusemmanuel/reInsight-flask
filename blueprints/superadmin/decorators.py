"""
=========================================================
Super Admin Decorators
=========================================================

Authorization decorators for the Super Admin module.
"""

from functools import wraps

from flask import (
    flash,
    redirect,
    url_for,
    abort
)

from flask_login import (
    current_user,
    login_required
)


# ==========================================================
# SUPER ADMIN REQUIRED
# ==========================================================

def superadmin_required(view):
    """
    Ensures that only Super Administrators
    can access a route.
    """

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        # User must exist
        if not current_user:

            flash(
                "Please login to continue.",
                "warning"
            )

            return redirect(
                url_for("superadmin.login")
            )

        # Account must be active
        if not current_user.is_active:

            flash(
                "Your account is inactive.",
                "danger"
            )

            return redirect(
                url_for("superadmin.login")
            )

        # Account must not be locked
        if current_user.is_locked:

            flash(
                "Your account has been locked.",
                "danger"
            )

            return redirect(
                url_for("superadmin.login")
            )

        # Must be Super Admin
        if not current_user.is_super_admin:

            abort(403)

        return view(*args, **kwargs)

    return wrapped_view


# ==========================================================
# VERIFIED EMAIL REQUIRED
# ==========================================================

def verified_email_required(view):
    """
    Allows access only to users whose email
    has been verified.
    """

    @wraps(view)
    @login_required
    def wrapped_view(*args, **kwargs):

        if not current_user.email_verified:

            flash(
                "Please verify your email address.",
                "warning"
            )

            return redirect(
                url_for("auth.verify_email")
            )

        return view(*args, **kwargs)

    return wrapped_view


# ==========================================================
# UNLOCKED ACCOUNT REQUIRED
# ==========================================================

def unlocked_required(view):
    """
    Prevents locked accounts from
    accessing Super Admin pages.
    """

    @wraps(view)
    @login_required
    def wrapped_view(*args, **kwargs):

        if current_user.is_locked:

            flash(
                "Your account has been locked.",
                "danger"
            )

            return redirect(
                url_for("auth.login")
            )

        return view(*args, **kwargs)

    return wrapped_view