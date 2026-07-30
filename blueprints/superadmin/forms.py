"""
=========================================================
Super Admin Forms
=========================================================

Forms used by the Super Administrator module.
"""

from flask_wtf import FlaskForm
from flask_wtf.file import (
    FileField,
    FileAllowed
)

from wtforms import (
    StringField,
    TextAreaField,
    EmailField,
    SelectField,
    BooleanField,
    IntegerField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    NumberRange,
    Optional
)


# ==========================================================
# PROFILE FORM
# ==========================================================

class SuperAdminProfileForm(FlaskForm):
    """
    Edit Super Admin profile.
    """

    photo = FileField(
        "Profile Picture",
        validators=[
            FileAllowed(
                ["jpg", "jpeg", "png", "webp"],
                "Images only."
            )
        ]
    )

    first_name = StringField(
        "First Name",
        validators=[
            DataRequired(),
            Length(max=100)
        ]
    )

    last_name = StringField(
        "Last Name",
        validators=[
            DataRequired(),
            Length(max=100)
        ]
    )

    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=4, max=50)
        ]
    )

    email = EmailField(
        "Email Address",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    phone = StringField(
        "Phone Number",
        validators=[
            Optional(),
            Length(max=20)
        ]
    )

    gender = SelectField(
        "Gender",
        choices=[
            ("", "Select Gender"),
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other")
        ]
    )

    bio = TextAreaField(
        "Biography",
        validators=[
            Optional(),
            Length(max=500)
        ]
    )

    submit = SubmitField(
        "Save Changes"
    )


# ==========================================================
# PLATFORM SETTINGS
# ==========================================================

class SuperAdminSettingsForm(FlaskForm):
    """
    Global platform settings.
    """

    platform_name = StringField(
        "Platform Name",
        validators=[DataRequired()]
    )

    platform_email = EmailField(
        "Platform Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    platform_phone = StringField(
        "Platform Phone"
    )

    platform_address = TextAreaField(
        "Platform Address"
    )

    enable_two_factor = BooleanField(
        "Enable Two-Factor Authentication"
    )

    require_email_verification = BooleanField(
        "Require Email Verification"
    )

    maximum_login_attempts = IntegerField(
        "Maximum Login Attempts",
        validators=[
            NumberRange(
                min=1,
                max=20
            )
        ]
    )

    session_timeout = IntegerField(
        "Session Timeout (Minutes)",
        validators=[
            NumberRange(
                min=5,
                max=1440
            )
        ]
    )

    smtp_host = StringField(
        "SMTP Host"
    )

    smtp_port = IntegerField(
        "SMTP Port"
    )

    smtp_ssl = BooleanField(
        "Use SSL/TLS"
    )

    maintenance_mode = BooleanField(
        "Maintenance Mode"
    )

    registration_open = BooleanField(
        "Allow School Registration"
    )

    debug_mode = BooleanField(
        "Debug Mode"
    )

    submit = SubmitField(
        "Save Settings"
    )


# ==========================================================
# SECURITY FORM
# ==========================================================

class SuperAdminSecurityForm(FlaskForm):
    """
    Security preferences.
    """

    two_factor_auth = BooleanField(
        "Enable Two-Factor Authentication"
    )

    email_login_alerts = BooleanField(
        "Email Login Alerts"
    )

    single_session = BooleanField(
        "Allow Only One Active Session"
    )

    submit = SubmitField(
        "Save Security Settings"
    )


# ==========================================================
# SEARCH FORM
# ==========================================================

class SearchForm(FlaskForm):
    """
    Search schools, users, subscriptions, etc.
    """

    keyword = StringField(
        "Search",
        validators=[
            Optional()
        ]
    )

    submit = SubmitField(
        "Search"
    )


# ==========================================================
# SYSTEM ANNOUNCEMENT
# ==========================================================

class AnnouncementForm(FlaskForm):
    """
    Send announcements to all users.
    """

    title = StringField(
        "Title",
        validators=[
            DataRequired(),
            Length(max=150)
        ]
    )

    message = TextAreaField(
        "Message",
        validators=[
            DataRequired(),
            Length(max=3000)
        ]
    )

    submit = SubmitField(
        "Publish Announcement"
    )