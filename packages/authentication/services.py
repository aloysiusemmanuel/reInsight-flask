"""
=========================================================
Authentication Services
=========================================================

Contains the business logic for authentication.

Responsibilities:
    - Authenticate users
    - Change passwords
    - Reset passwords
    - Send password reset emails
"""
from flask import (
    current_app,
    url_for
)

from packages.authentication.tokens import (
    generate_password_reset_token
)

from datetime import datetime

from sqlalchemy import or_ 

from packages.extensions import db

from packages.models.user import User


# ==========================================================
# AUTHENTICATE USER
# ==========================================================

def authenticate_user(login, password):
    """
    Authenticate a user using either username or email.
    """

    login = login.strip()

    user = User.query.filter(
        or_(
            User.username == login,
            User.email == login
        )
    ).first()

    if not user:
        return { "success": False,
                "user": user,
                "message": "Invalid username/email or password."}

    # Account inactive
    if not user.is_active:
        return {"success": False,
                "user": user,
                "message": "Account Is Inactive"}

    # Account locked
    if user.is_locked:
        return {"success": False,
                "user": user,
                "message":"Account is locked."}

    # Incorrect password
    if not user.check_password(password):

        user.record_failed_login()

        db.session.commit()

        return {"success": False,
                "user": user,
                "message":"Invalid username/email or password."}

    # Successful login

    user.record_successful_login()

    db.session.commit()

    return {
        "success": True,
        "user": user,
        "message": "Login successful."
    }


# ==========================================================
# CHANGE PASSWORD
# ==========================================================

def change_user_password(
    user,
    current_password,
    new_password
):
    """
    Changes the password for a logged-in user.
    """

    if not user.check_password(current_password):
        return False

    user.set_password(new_password)

    db.session.commit()

    return True


# ==========================================================
# RESET PASSWORD
# ==========================================================

def reset_user_password(
    user,
    new_password
):
    """
    Reset a user's password.
    """

    user.set_password(new_password)

    db.session.commit()

    return True


# ==========================================================
# SEND PASSWORD RESET EMAIL
# ==========================================================

def send_password_reset_email(email):
    """
    Sends a password reset email.

    Email functionality will be implemented later.
    """

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:
        return False

    token = generate_password_reset_token(user)
    reset_url = url_for(
    "auth.reset_password",
    token=token,
    _external=True
    )
    # TODO later
    # Email service:
    
    # send_email(

    # recipient=user.email,

    # subject="Password Reset",

    # template="emails/reset_password.html",

    # reset_url=reset_url,

    # user=user
    # )

    return True


# ==========================================================
# LOCK USER ACCOUNT
# ==========================================================

def lock_user(user):
    """
    Lock a user account.
    """

    user.is_locked = True

    db.session.commit()
    return {
    "success": True,
    "user": user,
    "message": "Login successful."
}


# ==========================================================
# UNLOCK USER ACCOUNT
# ==========================================================

def unlock_user(user):
    """
    Unlock a user account.
    """

    user.is_locked = False

    user.failed_login_attempts = 0

    db.session.commit()
    return {
    "success": True,
    "user": user,
    "message": "Login successful."
}


# ==========================================================
# ACTIVATE USER
# ==========================================================

def activate_user(user):
    """
    Activate a user account.
    """

    user.is_active = True

    db.session.commit()
    return {
                "success": True,
                "user": user,
                "message": "Login successful."
            }


# ==========================================================
# DEACTIVATE USER
# ==========================================================

def deactivate_user(user):
    """
    Deactivate a user account.
    """

    user.is_active = False

    db.session.commit()
    
    return {
    "success": True,
    "user": user,
    "message": "Login successful."
}


# ==========================================================
# UPDATE LAST LOGIN
# ==========================================================

def update_last_login(user):
    """
    Updates the user's last login time.
    """

    user.last_login = datetime.utcnow()

    db.session.commit()
    
    return {
    "success": True,
    "user": user,
    "message": "Login successful."
}