"""
=========================================================
Authentication Forms
=========================================================

Forms used for authentication in the reInsight
SaaS platform.
"""

from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length
)


# =========================================================
# LOGIN FORM
# =========================================================

class LoginForm(FlaskForm):
    """
    Login form.

    Allows login using either username or email.
    """

    login = StringField(
        "Username or Email",
        validators=[
            DataRequired(message="Enter your username or email.")
        ],
        render_kw={
            "placeholder": "Username or Email",
            "autocomplete": "username"
        }
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Enter your password.")
        ],
        render_kw={
            "placeholder": "Password",
            "autocomplete": "current-password"
        }
    )
    
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Passwords do not match."
            )
        ]
    )

    remember_me = BooleanField(
        "Remember Me"
    )

    submit = SubmitField(
        "Sign In"
    )


# =========================================================
# FORGOT PASSWORD
# =========================================================

class ForgotPasswordForm(FlaskForm):
    """
    Sends password reset link.
    """

    email = StringField(
        "Email Address",
        validators=[
            DataRequired(),
            Email()
        ],
        render_kw={
            "placeholder": "Email Address"
        }
    )

    submit = SubmitField(
        "Send Reset Link"
    )


# =========================================================
# RESET PASSWORD
# =========================================================

class ResetPasswordForm(FlaskForm):
    """
    Reset forgotten password.
    """

    password = PasswordField(
        "New Password",
        validators=[
            DataRequired(),
            Length(
                min=8,
                message="Password must be at least 8 characters."
            )
        ]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Passwords do not match."
            )
        ]
    )

    submit = SubmitField(
        "Reset Password"
    )


# =========================================================
# CHANGE PASSWORD
# =========================================================

class ChangePasswordForm(FlaskForm):
    """
    Change password while logged in.
    """

    current_password = PasswordField(
        "Current Password",
        validators=[
            DataRequired()
        ]
    )

    new_password = PasswordField(
        "New Password",
        validators=[
            DataRequired(),
            Length(
                min=8,
                message="Password must be at least 8 characters."
            )
        ]
    )

    confirm_password = PasswordField(
        "Confirm New Password",
        validators=[
            DataRequired(),
            EqualTo(
                "new_password",
                message="Passwords do not match."
            )
        ]
    )

    submit = SubmitField(
        "Change Password"
    )