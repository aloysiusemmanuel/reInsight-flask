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
    request
  
    
)
from werkzeug.security import check_password_hash, generate_password_hash

from flask_login import login_required, current_user, login_user, logout_user

from blueprints.superadmin import superadmin_bp
from .decorators import superadmin_required
from packages import db
from packages.models.school_admin import SchoolAdmin
from packages.models import User
from packages.authentication.services import authenticate_user





@superadmin_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:

        if current_user.is_super_admin:
            return redirect(
                url_for("superadmin.dashboard")
            )

        logout_user()

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        result = authenticate_user(
            username,
            password
        )

        if result["success"]:

            user = result["user"]

            # -----------------------------------------
            # SUPER ADMIN ONLY
            # -----------------------------------------

            if not user.is_super_admin:

                flash(
                    "You do not have permission to access the Super Admin portal.",
                    "danger"
                )

                return redirect(
                    url_for("superadmin.login")
                )

            login_user(user)

            return redirect(
                url_for("superadmin.dashboard")
            )

        flash(
            result["message"],
            "danger"
        )

    return render_template(
        "auth/superadmin_login.html"
    )
    
    
# ==========================================================
# DASHBOARD
# ==========================================================

@superadmin_bp.route("/dashboard")
@superadmin_required
def dashboard():

    return render_template(
        "superadmin/superadmin_dashboard.html"
    )


# ==========================================================
# PROFILE
# ==========================================================

@superadmin_bp.route("/profile")
@superadmin_required
def account_profile():

    return render_template(
        "superadmin_dash/account/profile.html"
    )


# ==========================================================
# EDIT ACCOUNT
# ==========================================================

@superadmin_bp.route("/profile/edit", methods=["GET", "POST"])
@superadmin_required
def account_edit_profile():

    if request.method == "POST":
        flash("Profile updated successfully.", "success")
        return redirect(url_for("superadmin.account-edit-profile"))

    return render_template(
        "superadmin_dash/account/edit_profile.html"
    )



# ==========================================================
# CHANGE PASSWORD
# ==========================================================

@superadmin_bp.route("/change-password", methods=["GET", "POST"])
# @superadmin_required
def change_password():

    if request.method == "POST":

        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")

        # Validate fields
        if not current_password or not new_password or not confirm_password:
            flash("All fields are required.", "danger")
            return redirect(url_for("superadmin.change_password"))

        # Check current password
        if not check_password_hash(current_user.password_hash, current_password):
            flash("Current password is incorrect.", "danger")
            return redirect(url_for("superadmin.change_password"))

        # Check password match
        if new_password != confirm_password:
            flash("New passwords do not match.", "danger")
            return redirect(url_for("superadmin.change_password"))

        # Check length
        if len(new_password) < 8:
            flash("Password must be at least 8 characters long.", "warning")
            return redirect(url_for("superadmin.change_password"))

        # Prevent using the same password
        if check_password_hash(current_user.password_hash, new_password):
            flash("New password must be different from the current password.", "warning")
            return redirect(url_for("superadmin.change_password"))

        # Update password
        current_user.password_hash = generate_password_hash(new_password)

        db.session.commit()

        flash("Password updated successfully.", "success")
        return redirect(url_for("superadmin.security"))

    return render_template(
        "superadmin_dash/account/change_password.html"
    )


# ==========================================================
# ACCOUNT SETTINGS
# ==========================================================
@superadmin_bp.route("/account/settings")
# @superadmin_required
def account_settings():
    return render_template(
        "superadmin_dash/account/settings.html"
    )



# ==========================================================
# SECURITY
# ==========================================================

@superadmin_bp.route("/security")
# @superadmin_required
def account_security():

    return render_template(
        "superadmin_dash/account/security.html"
    )


# ==========================================================
# NOTIFICATIONS
# ==========================================================

@superadmin_bp.route("/notifications")
# @superadmin_required
def account_notifications():

    return render_template(
        "superadmin_dash/account/notifications.html"
    )


# ==========================================================
# SCHOOL MANAGEMENT
# ==========================================================

@superadmin_bp.route("/schools")
@superadmin_required
def schools():

   return render_template("superadmin_dash/schools/home.html")


# ==========================================================
# REGISTER SCHOOL
# ==========================================================

@superadmin_bp.route("/schools/create", methods=["GET", "POST"])
@superadmin_required
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
@superadmin_required
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
@superadmin_required
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

@superadmin_bp.route("/platform", endpoint="platform-settings")
# @login_required
# @superadmin_required
def platform_settings():

    return render_template(
        "superadmin_dash/platform/platform_settings.html"
    )

# ==========================================================
# HELP CENTER
# ==========================================================

@superadmin_bp.route("/help-center")
# @login_required
# @superadmin_required
def help_center():

    return render_template(
        "superadmin_dash/help/help_center.html"
    )