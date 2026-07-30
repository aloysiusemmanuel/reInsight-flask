"""
=========================================================
Super Admin Routes
=========================================================

Platform Owner Dashboard

Accessible only by SUPER_ADMIN users.
"""

from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request,
)

from flask_login import login_required

from blueprints.superadmin import superadmin_bp
from .decorators import superadmin_required


# ==========================================================
# DASHBOARD
# ==========================================================

@superadmin_bp.route("/")
# @login_required
# @superadmin_required
def dashboard():

    return render_template(
        "superadmin/superadmin_dashboard.html"
    )


# ==========================================================
# PROFILE
# ==========================================================

@superadmin_bp.route("/profile")
# @login_required
# @superadmin_required
def profile():

    return render_template(
        "superadmin/superadmin_profile.html"
    )


# ==========================================================
# EDIT PROFILE
# ==========================================================

@superadmin_bp.route("/profile/edit", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def edit_profile():

    return render_template(
        "superadmin/superadmin_edit.html"
    )


# ==========================================================
# CHANGE PASSWORD
# ==========================================================

@superadmin_bp.route("/change-password", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def change_password():

    return render_template(
        "superadmin/superadmin_change_password.html"
    )


# ==========================================================
# SETTINGS
# ==========================================================

@superadmin_bp.route("/settings")
# @login_required
# @superadmin_required
def settings():

    return render_template(
        "superadmin/superadmin_settings.html"
    )


# ==========================================================
# SECURITY
# ==========================================================

@superadmin_bp.route("/security")
# @login_required
# @superadmin_required
def security():

    return render_template(
        "superadmin/superadmin_security.html"
    )


# ==========================================================
# NOTIFICATIONS
# ==========================================================

@superadmin_bp.route("/notifications")
# @login_required
# @superadmin_required
def notifications():

    return render_template(
        "superadmin/superadmin_notifications.html"
    )


# ==========================================================
# SCHOOL MANAGEMENT
# ==========================================================

@superadmin_bp.route("/schools")
# @login_required
# @superadmin_required
def schools():

    return render_template(
        "superadmin/schools.html"
    )


@superadmin_bp.route("/schools/create", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def create_school():

    return render_template(
        "superadmin/create_school.html"
    )
    
@superadmin_bp.route("/schools-admins/create", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def create_school_admin():

    return render_template(
        "superadmin/create_school_admin.html"
    )


@superadmin_bp.route("/schools/<int:id>")
# @login_required
# @superadmin_required
def school_details(id):

    return render_template(
        "superadmin/school_details.html"
    )


@superadmin_bp.route("/schools/<int:id>/edit", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def edit_school(id):

    return render_template(
        "superadmin/edit_school.html"
    )


# ==========================================================
# USER MANAGEMENT
# ==========================================================

@superadmin_bp.route("/users")
# @login_required
# @superadmin_required
def users():

    return render_template(
        "superadmin/users.html"
    )


@superadmin_bp.route("/users/create", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def create_user():

    return render_template(
        "superadmin/create_user.html"
    )


@superadmin_bp.route("/users/<int:id>")
# @login_required
# @superadmin_required
def user_details(id):

    return render_template(
        "superadmin/user_details.html"
    )


@superadmin_bp.route("/users/<int:id>/edit", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def edit_user(id):

    return render_template(
        "superadmin/edit_user.html"
    )


# ==========================================================
# ROLES
# ==========================================================

@superadmin_bp.route("/roles")
# @login_required
# @superadmin_required
def roles():

    return render_template(
        "superadmin/roles.html"
    )


@superadmin_bp.route("/roles/create", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def create_role():

    return render_template(
        "superadmin/create_role.html"
    )


# ==========================================================
# PERMISSIONS
# ==========================================================

@superadmin_bp.route("/permissions")
# @login_required
# @superadmin_required
def permissions():

    return render_template(
        "superadmin/permissions.html"
    )


# ==========================================================
# SUBSCRIPTIONS
# ==========================================================

@superadmin_bp.route("/subscriptions")
# @login_required
# @superadmin_required
def subscriptions():

    return render_template(
        "superadmin/subscriptions.html"
    )

@superadmin_bp.route("/subscriptions/create")
# @login_required
# @superadmin_required
def subscription_create():

    return render_template(
        "superadmin/subscriptions_create.html"
    )

# ==========================================================
# PAYMENTS
# ==========================================================

@superadmin_bp.route("/payments")
# @login_required
# @superadmin_required
def payments():

    return render_template(
        "superadmin/payments.html"
    )


# ==========================================================
# REPORTS
# ==========================================================

@superadmin_bp.route("/reports")
# @login_required
# @superadmin_required
def reports():

    return render_template(
        "superadmin/reports.html"
    )


# ==========================================================
# AUDIT LOGS
# ==========================================================

@superadmin_bp.route("/audit-logs")
# @login_required
# @superadmin_required
def audit_logs():

    return render_template(
        "superadmin/audit_logs.html"
    )


# ==========================================================
# SYSTEM SETTINGS
# ==========================================================

@superadmin_bp.route("/system")
# @login_required
# @superadmin_required
def system():

    return render_template(
        "superadmin/system.html"
    )


# ==========================================================
# BACKUPS
# ==========================================================

@superadmin_bp.route("/backups")
# @login_required
# @superadmin_required
def backups():

    return render_template(
        "superadmin/backups.html"
    )


# ==========================================================
# PLATFORM SETTINGS
# ==========================================================

@superadmin_bp.route("/platform")
# @login_required
# @superadmin_required
def platform():

    return render_template(
        "superadmin/platform.html"
    )


# ==========================================================
# HELP
# ==========================================================

@superadmin_bp.route("/help")
# @login_required
# @superadmin_required
def help_center():

    return render_template(
        "superadmin/help.html"
    )