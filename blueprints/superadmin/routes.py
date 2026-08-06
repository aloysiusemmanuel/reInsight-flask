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

   return render_template("superadmin_dash/schools/home.html")


# ==========================================================
# REGISTER SCHOOL
# ==========================================================

@superadmin_bp.route("/schools/create", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def create_school():

    if request.method == "POST":
        flash("School registered successfully.", "success")
        return redirect(url_for("superadmin.schools"))

    return render_template(
        "superadmin_dash/schools/create.html"
    )
    
# ==========================================================
# CREATE SCHOOL ADMINISTRATOR
# ==========================================================

@superadmin_bp.route("/schools-admins/create", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def create_school_admin():

    if request.method == "POST":
        flash("School administrator created successfully.", "success")
        return redirect(url_for("superadmin.schools"))

    return render_template(
        "superadmin_dash/schools/create_school_admin.html"
    )


# ==========================================================
# SCHOOL DETAILS
# ==========================================================

@superadmin_bp.route("/schools/<int:id>")
# @login_required
# @superadmin_required
def school_details(id):

    school = {
        "id": id,
        "name": "Greenfield College",
        "code": "SCH-001",
        "status": "Active",
        "plan": "Premium",
        "email": "info@greenfield.edu.ng",
        "phone": "+234 801 234 5678",
        "school_type": "Primary & Secondary",
        "ownership": "Private",
        "address": "12 Allen Avenue, Ikeja, Lagos",
        "country": "Nigeria",
        "state": "Lagos",
        "city": "Ikeja",
        "students": 1240,
        "teachers": 68,
        "revenue": "₦450,000",
        "billing": "Yearly",
        "start_date": "01 Jan 2026",
        "expiry_display": "31 Dec 2026",
        "admin_name": "Mrs. Sarah Johnson",
        "admin_email": "admin@greenfield.edu.ng"
    }

    return render_template(
        "superadmin_dash/schools/school_details.html",
        school=school
    )


# ==========================================================
# EDIT SCHOOL
# ==========================================================

@superadmin_bp.route("/schools/<int:id>/edit", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def edit_school(id):

    school = {
        "id": id,
        "name": "Greenfield College",
        "code": "SCH-001",
        "email": "info@greenfield.edu.ng",
        "phone": "+234 801 234 5678",
        "school_type": "Primary & Secondary",
        "ownership": "Private",
        "address": "12 Allen Avenue, Ikeja, Lagos",
        "country": "Nigeria",
        "state": "Lagos",
        "city": "Ikeja",
        "plan": "Premium",
        "status": "Active",
        "expiry_date": "2026-12-31",
        "students": 1240,
        "teachers": 68,
        "created": "15 Jan 2025"
    }

    if request.method == "POST":
        flash("School updated successfully.", "success")
        return redirect(url_for("superadmin.school_details", id=id))

    return render_template(
        "superadmin_dash/schools/edit.html",
        school=school
    )


# ==========================================================
# USER MANAGEMENT
# ==========================================================

@superadmin_bp.route("/users")
# @login_required
# @superadmin_required
def users():

    return render_template(
        "superadmin_dash/users/home.html"
    )


# ==========================================================
# CREATE USER
# ==========================================================

@superadmin_bp.route("/users/create", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def create_user():

    if request.method == "POST":
        flash("User created successfully.", "success")
        return redirect(url_for("superadmin.users"))

    return render_template(
        "superadmin_dash/users/create_user.html"
    )


# ==========================================================
# USER DETAILS
# ==========================================================

@superadmin_bp.route("/users/<int:id>")
# @login_required
# @superadmin_required
def user_details(id):

    user = {
        "id": id,
        "name": "David James",
        "username": "davidjames",
        "email": "david.james@school.com",
        "phone": "+234 801 234 5678",
        "gender": "Male",
        "role": "School Admin",
        "status": "Active",
        "school": "Greenfield College",
        "school_code": "SCH-001",
        "joined": "15 Jan 2025",
        "last_login": "Today · 08:15 AM",
        "activity": "24 actions",
        "security": "2FA Enabled",
        "two_factor": "Enabled"
    }

    return render_template(
        "superadmin_dash/users/user_details.html",
        user=user
    )


# ==========================================================
# EDIT USER
# ==========================================================

@superadmin_bp.route("/users/<int:id>/edit", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def edit_user(id):

    user = {
        "id": id,
        "first_name": "David",
        "last_name": "James",
        "username": "davidjames",
        "email": "david.james@school.com",
        "phone": "+234 801 234 5678",
        "gender": "Male",
        "role": "School Admin",
        "status": "Active",
        "school": "Greenfield College",
        "two_factor": "Enabled"
    }

    if request.method == "POST":
        flash("User updated successfully.", "success")
        return redirect(url_for("superadmin.user_details", id=id))

    return render_template(
        "superadmin_dash/users/edit_user.html",
        user=user
    )


# ==========================================================
# ROLES
# ==========================================================

@superadmin_bp.route("/roles")
# @login_required
# @superadmin_required
def roles():

    return render_template(
        "superadmin_dash/users/roles.html"
    )


# ==========================================================
# CREATE ROLE
# ==========================================================

@superadmin_bp.route("/roles/create", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def create_role():

    if request.method == "POST":
        flash("Role created successfully.", "success")
        return redirect(url_for("superadmin.roles"))

    return render_template(
        "superadmin_dash/users/create_role.html"
    )



# ==========================================================
# PERMISSIONS
# ==========================================================

@superadmin_bp.route("/permissions")
# @login_required
# @superadmin_required
def permissions():
    return render_template("superadmin_dash/users/permissions.html")


# ==========================================================
# SUBSCRIPTIONS
# ==========================================================

@superadmin_bp.route("/subscriptions")
# @login_required
# @superadmin_required
def subscriptions():

    return render_template(
        "superadmin_dash/business/subscriptions.html"
    )

# ==========================================================
# CREATE SUBSCRIPTION
# ==========================================================

@superadmin_bp.route("/subscriptions/create", methods=["GET", "POST"])
# @login_required
# @superadmin_required
def subscription_create():

    if request.method == "POST":
        flash("Subscription created successfully.", "success")
        return redirect(url_for("superadmin.subscriptions"))

    return render_template(
        "superadmin_dash/business/subscription_create.html"
    )

# ==========================================================
# PAYMENTS
# ==========================================================

@superadmin_bp.route("/payments")
# @login_required
# @superadmin_required
def payments():

    return render_template(
        "superadmin_dash/business/payments.html"
    )

# ==========================================================
# REPORTS
# ==========================================================

@superadmin_bp.route("/reports")
# @login_required
# @superadmin_required
def reports():

    return render_template(
        "superadmin_dash/reports/home.html"
    )



# ==========================================================
# AUDIT LOGS
# ==========================================================

@superadmin_bp.route("/audit-logs")
# @login_required
# @superadmin_required
def audit_logs():

    return render_template(
        "superadmin_dash/reports/audit_logs.html"
    )


# ==========================================================
# SYSTEM SETTINGS
# ==========================================================

@superadmin_bp.route("/system")
# @login_required
# @superadmin_required
def system():

    return render_template(
        "superadmin_dash/platform/system.html"
    )


# ==========================================================
# BACKUPS
# ==========================================================

@superadmin_bp.route("/backups")
# @login_required
# @superadmin_required
def backups():

    return render_template(
        "superadmin_dash/platform/backups.html"
    )


# ==========================================================
# PLATFORM SETTINGS
# ==========================================================

@superadmin_bp.route("/platform")
# @login_required
# @superadmin_required
def platform():

    return render_template(
        "superadmin_dash/platform/platform.html"
    )

@superadmin_bp.route("/platform")
def platform_settings():
    return render_template("superadmin_dash/platform/settings.html")

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