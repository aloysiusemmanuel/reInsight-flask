"""
=========================================================
Authentication Exceptions
=========================================================

Custom exceptions for the reInsight SaaS platform.

These exceptions provide meaningful error handling for
authentication and authorization processes.
"""


# ==========================================================
# BASE AUTHENTICATION EXCEPTION
# ==========================================================

class AuthenticationError(Exception):
    """
    Base exception for all authentication-related errors.
    """
    pass


# ==========================================================
# INVALID CREDENTIALS
# ==========================================================

class InvalidCredentialsError(AuthenticationError):
    """
    Raised when the username/email or password is incorrect.
    """
    pass


# ==========================================================
# ACCOUNT LOCKED
# ==========================================================

class AccountLockedError(AuthenticationError):
    """
    Raised when a user account has been locked.
    """
    pass


# ==========================================================
# ACCOUNT INACTIVE
# ==========================================================

class InactiveAccountError(AuthenticationError):
    """
    Raised when the account is inactive.
    """
    pass


# ==========================================================
# EMAIL NOT VERIFIED
# ==========================================================

class EmailNotVerifiedError(AuthenticationError):
    """
    Raised when the user's email has not been verified.
    """
    pass


# ==========================================================
# PASSWORD RESET TOKEN
# ==========================================================

class InvalidResetTokenError(AuthenticationError):
    """
    Raised when a password reset token is invalid.
    """
    pass


class ExpiredResetTokenError(AuthenticationError):
    """
    Raised when a password reset token has expired.
    """
    pass


# ==========================================================
# PERMISSION ERRORS
# ==========================================================

class PermissionDeniedError(AuthenticationError):
    """
    Raised when a user attempts to access a resource
    without sufficient permission.
    """
    pass


class InvalidRoleError(AuthenticationError):
    """
    Raised when the user's role is not authorized.
    """
    pass


# ==========================================================
# SCHOOL ERRORS
# ==========================================================

class SchoolInactiveError(AuthenticationError):
    """
    Raised when a school's account has been deactivated.
    """
    pass


class SubscriptionExpiredError(AuthenticationError):
    """
    Raised when a school's subscription has expired.
    """
    pass


# ==========================================================
# USER ERRORS
# ==========================================================

class UserNotFoundError(AuthenticationError):
    """
    Raised when the requested user cannot be found.
    """
    pass


class DuplicateUserError(AuthenticationError):
    """
    Raised when attempting to create a duplicate user.
    """
    pass