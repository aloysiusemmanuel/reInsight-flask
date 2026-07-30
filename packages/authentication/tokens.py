"""
=========================================================
Authentication Tokens
=========================================================

Generates and verifies secure tokens for:

    - Password Reset
    - Email Verification
    - Invitations (future)

Uses itsdangerous for secure, time-limited tokens.
"""

from itsdangerous import (
    URLSafeTimedSerializer,
    BadSignature,
    SignatureExpired
)

from flask import current_app


# ==========================================================
# SERIALIZER
# ==========================================================

def get_serializer():
    """
    Returns the application's secure serializer.
    """
    return URLSafeTimedSerializer(
        current_app.config["SECRET_KEY"]
    )


# ==========================================================
# PASSWORD RESET TOKEN
# ==========================================================

def generate_password_reset_token(user):
    """
    Generate a secure password reset token.
    """

    serializer = get_serializer()

    return serializer.dumps(
        {
            "user_id": user.id,
            "school_id": user.school_id,
            "role": user.role.name
        },
        salt="password-reset"
    )


def verify_password_reset_token(
    token,
    expiration=3600
):
    """
    Verify a password reset token.

    Default expiration:
        3600 seconds (1 hour)

    Returns:
        user_id or None
    """

    serializer = get_serializer()

    try:

        user_id = serializer.loads(
            token,
            salt="password-reset",
            max_age=expiration
        )

        return user_id

    except SignatureExpired:
        return None

    except BadSignature:
        return None


# ==========================================================
# EMAIL VERIFICATION TOKEN
# ==========================================================

def generate_email_verification_token(user):
    """
    Generate email verification token.
    """

    serializer = get_serializer()

    return serializer.dumps(
        user.id,
        salt="email-verification"
    )


def verify_email_verification_token(
    token,
    expiration=86400
):
    """
    Verify email verification token.

    Default:
        24 hours
    """

    serializer = get_serializer()

    try:

        user_id = serializer.loads(
            token,
            salt="email-verification",
            max_age=expiration
        )

        return user_id

    except SignatureExpired:
        return None

    except BadSignature:
        return None


# ==========================================================
# INVITATION TOKEN (Future)
# ==========================================================

def generate_invitation_token(
    user,
    invitation_type="user"
):
    """
    Generate invitation token.

    Examples:

        teacher

        parent

        school_admin
    """

    serializer = get_serializer()

    return serializer.dumps(
        {
            "user_id": user.id,
            "type": invitation_type
        },
        salt="invitation"
    )


def verify_invitation_token(
    token,
    expiration=604800
):
    """
    Verify invitation token.

    Default expiration:
        7 days
    """

    serializer = get_serializer()

    try:

        data = serializer.loads(
            token,
            salt="invitation",
            max_age=expiration
        )

        return {
                "user_id": data["user_id"],
                "school_id": data["school_id"],
                "role": data["role"]
        }


    except SignatureExpired:
        return None

    except BadSignature:
        return None