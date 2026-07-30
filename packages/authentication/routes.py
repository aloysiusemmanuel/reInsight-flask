"""
=========================================================
Authentication Routes
=========================================================

Handles:

- Login
- Logout
- Forgot Password
- Reset Password
- Change Password
"""

from flask import (
    render_template,
    redirect,
    flash,
    request,
    url_for,
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from . import auth_bp

from .forms import (
    LoginForm,
    ForgotPasswordForm,
    ResetPasswordForm,
    ChangePasswordForm
)

from .services import (
    authenticate_user,
    send_password_reset_email,
    reset_user_password,
    change_user_password
)
from .utils import get_dashboard_url

#===================================================
# LOGIN ROUTE
# ================================================

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """
    User Login
    """

    if current_user.is_authenticated:
        return redirect(get_dashboard_url(current_user))

    form = LoginForm()

    if form.validate_on_submit():

        result = authenticate_user(
            form.login.data,
            form.password.data
        )

        if result["success"]:
            print(result)
            print(result.get("user"))

            login_user(
                result["user"],
                remember=form.remember_me.data
            )

            flash(result["message"], "success")

            next_page = request.args.get("next")

            if next_page:
                return redirect(next_page)

            return redirect(
                get_dashboard_url(result["user"])
            )

        flash(result["message"], "danger")

    return render_template(
        "auth/login.html",
        form=form
    )


    
    
    
#===================================================
# LOGOUT ROUTE
# ==================================================

@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "You have been logged out.",
        "info"
    )

    return redirect(
        url_for("auth.login")
    )
    
#===================================================
# FORGOT PASSWORD ROUTE
# ==================================================

@auth_bp.route(
    "/forgot-password",
    methods=["GET", "POST"]
)
def forgot_password():

    form = ForgotPasswordForm()

    if form.validate_on_submit():

        send_password_reset_email(
            form.email.data
        )

        flash(
            "If the account exists, a reset link has been sent.",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "auth/forgot_password.html",
        form=form
    )
    
    
#===================================================
# RESET PASSWORD ROUTE
# ==================================================

@auth_bp.route(
    "/reset-password/<token>",
    methods=["GET", "POST"]
)
def reset_password(token):

    form = ResetPasswordForm()

    if form.validate_on_submit():

        if reset_user_password(
            token,
            form.password.data
        ):

            flash(
                "Password reset successfully.",
                "success"
            )

            return redirect(
                url_for("auth.login")
            )

        flash(
            "Invalid or expired reset link.",
            "danger"
        )

    return render_template(
        "auth/reset_password.html",
        form=form
    )
    
 #===================================================
# CHANGE PASSWORD ROUTE
# ==================================================  

@auth_bp.route(
    "/change-password",
    methods=["GET", "POST"]
)
@login_required
def change_password():

    form = ChangePasswordForm()

    if form.validate_on_submit():

        success = change_user_password(
            current_user,
            form.current_password.data,
            form.new_password.data
        )

        if success:

            flash(
                "Password changed successfully.",
                "success"
            )

            return redirect(
                get_dashboard_url(current_user)
            )

        flash(
            "Current password is incorrect.",
            "danger"
        )

    return render_template(
        "auth/change_password.html",
        form=form
    ) 
    
    
#===================================================
# VERIFICATION ROUTE
# ==================================================  

@auth_bp.route("/verify-email")
def verify_email():
    ...

@auth_bp.route("/verify-email/<token>")
def verify_email_token(token):
    ...

@auth_bp.route("/resend-verification")
@login_required
def resend_verification():
    ...