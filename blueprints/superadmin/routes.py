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

from datetime import datetime

from flask_login import login_required, current_user, login_user, logout_user

from blueprints.superadmin import superadmin_bp
from .decorators import superadmin_required
from packages import db
from packages.models import School
from packages.models.school_admin import SchoolAdmin
from packages.models import User
from packages.authentication.services import authenticate_user

#==================================================================
# ROUTE FOR SUPERADMIN WHEN I ENTER JUST SUPERADMIN AND SUPERADMIN/LOGIN
#==================================================================

@superadmin_bp.route("/")
def superadmin():
    
    return redirect(
        url_for("superadmin.login")
    )

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
        password = request.form.get("password", "").strip()

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

    total_schools = School.query.count()

    active_schools = School.query.filter_by(
        subscription_status="Active"
    ).count()

    trial_schools = School.query.filter_by(
        subscription_status="Trial"
    ).count()

    suspended_schools = School.query.filter_by(
        subscription_status="Suspended"
    ).count()
    
    pending_schools = School.query.filter_by(
            subscription_status="pending"
        ).count()

    return render_template(
        "superadmin/superadmin_dashboard.html",

        total_schools=total_schools,

        active_schools=active_schools,

        trial_schools=trial_schools,

        suspended_schools=suspended_schools,
        
        pending_schools=pending_schools
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
@superadmin_required
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
@superadmin_required
def account_settings():
    return render_template(
        "superadmin_dash/account/settings.html"
    )



# ==========================================================
# SECURITY
# ==========================================================

@superadmin_bp.route("/security")
@superadmin_required
def account_security():

    return render_template(
        "superadmin_dash/account/security.html"
    )


# ==========================================================
# NOTIFICATIONS
# ==========================================================

@superadmin_bp.route("/notifications")
@superadmin_required
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
    
    schools = (
        School.query
        .order_by(School.id.desc())
        .all()
    )
    
    total_schools = School.query.count()
    
    active_schools = School.query.filter_by(
            subscription_status="Active"
        ).count()
    
    trial_schools = School.query.filter_by(
            subscription_status="Trial"
        ).count()
    
    suspended_schools = School.query.filter_by(
            subscription_status="Suspended"
        ).count()
        
    pending_schools = School.query.filter_by(
                subscription_status="pending"
            ).count()

    return render_template(
    "superadmin_dash/schools/home.html",
    schools=schools,
    total_schools=total_schools,
    active_schools=active_schools,
    trial_schools=trial_schools,
    suspended_schools=suspended_schools,
    pending_schools=pending_schools 
)


# ==========================================================
# REGISTER SCHOOL
# ==========================================================


@superadmin_bp.route("/schools/create", methods=["GET", "POST"])
@superadmin_required
def create_school():

    if request.method == "POST":

        try:

            # =====================================================
            # Collect FORM DATA FROM Superadmin Create School page
            # =====================================================

            name = request.form.get("name", "").strip()
            email = request.form.get("email", "").strip()
            phone = request.form.get("phone", "").strip()
            code = request.form.get("code", "").strip()
            website = request.form.get("website", "").strip()
            address = request.form.get("address", "").strip()
            city = request.form.get("city", "").strip()
            state = request.form.get("state", "").strip()
            country = request.form.get("country","Nigeria").strip()
            postal_code = request.form.get("postal_code","").strip()
            school_type = request.form.get("school_type","Secondary").strip()
            ownership = request.form.get("ownership","").strip()
            motto = request.form.get("motto","").strip()
            established_year = request.form.get("established_year", "").strip()

            # =====================================================
            # VALIDATION OF THE INPUT FORMS
            # =====================================================

            if not name:
                flash(
                    "School name is required.",
                    "danger"
                )

                return redirect(
                    url_for("superadmin.create_school")
                )

            if not email:
                flash(
                    "School email is required.",
                    "danger"
                )

                return redirect(
                    url_for("superadmin.create_school")
                )

            if not phone:
                flash(
                    "School phone number is required.",
                    "danger"
                )

                return redirect(
                    url_for("superadmin.create_school")
                )

            if not address:
                flash(
                    "School address is required.",
                    "danger"
                )

                return redirect(
                    url_for("superadmin.create_school")
                )

            # =====================================================
            # CHECK DUPLICATES
            # =====================================================

            existing_email = School.query.filter_by(
                email=email
            ).first()

            if existing_email:

                flash(
                    "A school with this email already exists.",
                    "danger"
                )

                return render_template(
                    "superadmin_dash/schools/create.html"
                )

            # =====================================================
            # GENERATE SLUG
            # =====================================================

            slug = name.lower().strip()

            slug = slug.replace(" ", "-")

            # =====================================================
            # CHECK SLUG
            # =====================================================

            existing_slug = School.query.filter_by(
                slug=slug
            ).first()

            if existing_slug:

                flash(
                    "A school with this name already exists.",
                    "danger"
                )

                return render_template(
                    "superadmin_dash/schools/create.html"
                )

            # =====================================================
            # ESTABLISHED YEAR
            # =====================================================

            if established_year:

                established_year = int(
                    established_year
                )

            else:

                established_year = None

            # =====================================================
            # CREATE SCHOOL
            # =====================================================

            school = School(

                name=name,

                slug=slug,
                
                code=code,

                email=email,

                phone=phone,

                website=website or None,

                address=address,

                city=city or None,

                state=state or None,

                country=country,

                postal_code=postal_code or None,

                school_type=school_type,

                ownership=ownership or None,

                motto=motto or None,

                established_year=established_year,

                subscription_plan="Demo",

                subscription_status="Pending"

            )

            # =====================================================
            # SAVE
            # =====================================================

            db.session.add(school)
            
            db.session.flush()
            
            school.code = f"SCH-{datetime.now()}-{school.id:03d}"
            
            db.session.commit()

            flash(
                f"{school.name} was registered successfully "
                f"with school code {school.code}.",
                "success"
            )

            return redirect(
                url_for("superadmin.schools")
            )

        except ValueError:

            db.session.rollback()

            flash(
                "Established year must be a valid number.",
                "danger"
            )

        except Exception as e:

            db.session.rollback()
            
            print("ERROR CREATING SCHOOL:", e)

            flash(
                f"Error registering school: {str(e)}",
                "danger"
            )

    return render_template(
        "superadmin_dash/schools/create.html"
    )
    
# ==========================================================
# CREATE SCHOOL ADMINISTRATOR
# ==========================================================

@superadmin_bp.route("/schools-admins/create", methods=["GET", "POST"])
@superadmin_required
def create_school_admin():
    
    
    schools = (
            School.query
            .order_by(School.id.desc())
            .all()
        )

    if request.method == "POST":
        flash("School administrator created successfully.", "success")
        return redirect(url_for("superadmin.userss"))

    return render_template(
        "superadmin_dash/schools/create_school_admin.html", schools=schools
    )


# ==========================================================
# SCHOOL DETAILS
# ==========================================================

@superadmin_bp.route("/schools/<int:id>")
@superadmin_required
def school_details(id):
    
    school = (
        School.query
        .order_by(School.id.desc())
        .all()
    )

    # school = {
    #     "id": id,
    #     "name": "Greenfield College",
    #     "code": "SCH-001",
    #     "status": "Active",
    #     "plan": "Premium",
    #     "email": "info@greenfield.edu.ng",
    #     "phone": "+234 801 234 5678",
    #     "school_type": "Primary & Secondary",
    #     "ownership": "Private",
    #     "address": "12 Allen Avenue, Ikeja, Lagos",
    #     "country": "Nigeria",
    #     "state": "Lagos",
    #     "city": "Ikeja",
    #     "students": 1240,
    #     "teachers": 68,
    #     "revenue": "₦450,000",
    #     "billing": "Yearly",
    #     "start_date": "01 Jan 2026",
    #     "expiry_display": "31 Dec 2026",
    #     "admin_name": "Mrs. Sarah Johnson",
    #     "admin_email": "admin@greenfield.edu.ng"
    # }

    return render_template(
        "superadmin_dash/schools/school_details.html",
        school=school,
        id=id
    )


# ==========================================================
# EDIT SCHOOL
# ==========================================================

@superadmin_bp.route("/schools/<int:id>/edit", methods=["GET", "POST"])
@superadmin_required
def edit_school(id):

    school = School.query.get_or_404(id)

    if request.method == "POST":

        school.name = request.form.get("name", "").strip()
        school.email = request.form.get("email", "").strip()
        school.phone = request.form.get("phone", "").strip()
        school.website = request.form.get("website", "").strip()

        school.address = request.form.get("address", "").strip()
        school.city = request.form.get("city", "").strip()
        school.state = request.form.get("state", "").strip()
        school.country = request.form.get("country", "").strip()

        school.school_type = request.form.get("school_type", "").strip()
        school.ownership = request.form.get("ownership", "").strip()
        school.motto = request.form.get("motto", "").strip()

        db.session.commit()

        flash(
            "School updated successfully.",
            "success"
        )

        return redirect(
            url_for("superadmin.schools")
        )

    return render_template(
        "superadmin_dash/schools/edit.html",
        school=school,
        id=id
    )


# ==========================================================
# USER MANAGEMENT
# ==========================================================

@superadmin_bp.route("/users")
@superadmin_required
def users():

    return render_template(
        "superadmin_dash/users/home.html"
    )


# ==========================================================
# CREATE USER
# ==========================================================

@superadmin_bp.route("/users/create", methods=["GET", "POST"])
@superadmin_required
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
@superadmin_required
def user_details(id):
    

    user = (User.query.order_by(User.id.all()))

    return render_template(
        "superadmin_dash/users/user_details.html",
        user=user,
        id=id
    )


# ==========================================================
# EDIT USER
# ==========================================================

@superadmin_bp.route("/users/<int:id>/edit", methods=["GET", "POST"])
@superadmin_required
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
@superadmin_required
def roles():

    return render_template(
        "superadmin_dash/users/roles.html"
    )


# ==========================================================
# CREATE ROLE
# ==========================================================

@superadmin_bp.route("/roles/create", methods=["GET", "POST"])
@superadmin_required
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
@superadmin_required
def permissions():
    return render_template("superadmin_dash/users/permissions.html")


# ==========================================================
# SUBSCRIPTIONS
# ==========================================================

@superadmin_bp.route("/subscriptions")
@superadmin_required
def subscriptions():

    return render_template(
        "superadmin_dash/business/subscriptions.html"
    )

# ==========================================================
# CREATE SUBSCRIPTION
# ==========================================================

@superadmin_bp.route("/subscriptions/create", methods=["GET", "POST"])
@superadmin_required
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
@superadmin_required
def payments():

    return render_template(
        "superadmin_dash/business/payments.html"
    )

# ==========================================================
# REPORTS
# ==========================================================

@superadmin_bp.route("/reports")
@superadmin_required
def reports():

    return render_template(
        "superadmin_dash/reports/home.html"
    )



# ==========================================================
# AUDIT LOGS
# ==========================================================

@superadmin_bp.route("/audit-logs")
@superadmin_required
def audit_logs():

    return render_template(
        "superadmin_dash/reports/audit_logs.html"
    )


# ==========================================================
# SYSTEM SETTINGS
# ==========================================================

@superadmin_bp.route("/system")
@superadmin_required
def system():

    return render_template(
        "superadmin_dash/platform/system.html"
    )


# ==========================================================
# BACKUPS
# ==========================================================

@superadmin_bp.route("/backups")
@superadmin_required
def backups():

    return render_template(
        "superadmin_dash/platform/backups.html"
    )



# ==========================================================
# PLATFORM SETTINGS
# ==========================================================

@superadmin_bp.route("/platform", endpoint="platform-settings")
@superadmin_required
def platform_settings():

    return render_template(
        "superadmin_dash/platform/platform_settings.html"
    )

# ==========================================================
# HELP CENTER
# ==========================================================

@superadmin_bp.route("/help-center")
@superadmin_required
def help_center():

    return render_template(
        "superadmin_dash/help/help_center.html"
    )

#===================================================
# LOGOUT ROUTE
# ==================================================

@superadmin_bp.route("/logout")
@superadmin_required
def logout():

    logout_user()

    flash(
        "You have been logged out.",
        "info"
    )

    return redirect(
        url_for("superadmin.login")
    )