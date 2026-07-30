"""
=========================================================
Super Admin Utilities
=========================================================

Utility functions used throughout the Super Admin module.
"""

from datetime import datetime
from uuid import uuid4

from flask import current_app

from werkzeug.utils import secure_filename


# ==========================================================
# GENERATE UNIQUE FILENAME
# ==========================================================

def generate_filename(filename):
    """
    Generates a unique filename while preserving
    the original extension.
    """

    extension = filename.rsplit(".", 1)[-1].lower()

    unique_name = uuid4().hex

    return f"{unique_name}.{extension}"


# ==========================================================
# SAVE PROFILE IMAGE
# ==========================================================

def save_profile_image(file):
    """
    Generates a secure filename.

    Actual file saving can be implemented later.
    """

    filename = secure_filename(file.filename)

    return generate_filename(filename)


# ==========================================================
# FORMAT DATETIME
# ==========================================================

def format_datetime(value, fmt="%d %b %Y %I:%M %p"):
    """
    Format datetime for templates.
    """

    if not value:
        return "-"

    return value.strftime(fmt)


# ==========================================================
# FORMAT DATE
# ==========================================================

def format_date(value):
    """
    Format date only.
    """

    if not value:
        return "-"

    return value.strftime("%d %b %Y")


# ==========================================================
# FORMAT TIME
# ==========================================================

def format_time(value):
    """
    Format time only.
    """

    if not value:
        return "-"

    return value.strftime("%I:%M %p")


# ==========================================================
# CURRENT DATETIME
# ==========================================================

def current_datetime():
    """
    Returns current UTC datetime.
    """

    return datetime.utcnow()


# ==========================================================
# DASHBOARD GREETING
# ==========================================================

def dashboard_greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "Good Morning"

    if hour < 17:
        return "Good Afternoon"

    return "Good Evening"


# ==========================================================
# APPLICATION NAME
# ==========================================================

def app_name():

    return current_app.config.get(
        "APP_NAME",
        "reInsight"
    )


# ==========================================================
# BOOLEAN BADGE
# ==========================================================

def status_badge(status):
    """
    Returns Bootstrap badge class.
    """

    return "success" if status else "danger"


# ==========================================================
# USER STATUS
# ==========================================================

def user_status(user):
    """
    Returns user account status.
    """

    if user.is_locked:
        return "Locked"

    if not user.is_active:
        return "Inactive"

    return "Active"


# ==========================================================
# STORAGE SIZE
# ==========================================================

def human_filesize(size):
    """
    Converts bytes to human-readable size.
    """

    units = ["B", "KB", "MB", "GB", "TB"]

    for unit in units:

        if size < 1024:

            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} PB"


# ==========================================================
# PERCENTAGE
# ==========================================================

def percentage(value, total):
    """
    Calculates percentage.
    """

    if total == 0:
        return 0

    return round((value / total) * 100, 2)


# ==========================================================
# GENERATE REFERENCE NUMBER
# ==========================================================

def generate_reference(prefix="REF"):
    """
    Example:
        REF-20260723-4F7A9B
    """

    date = datetime.now().strftime("%Y%m%d")

    code = uuid4().hex[:6].upper()

    return f"{prefix}-{date}-{code}"


# ==========================================================
# PLATFORM VERSION
# ==========================================================

def platform_version():

    return current_app.config.get(
        "VERSION",
        "1.0.0"
    )