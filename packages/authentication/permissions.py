"""
=========================================================
Authorization Permissions
=========================================================

Permission helper functions for the reInsight SaaS
platform.

These helpers are used throughout the application to
check whether a user can perform a specific action.
"""

from flask_login import current_user


# ==========================================================
# ROLE CHECKS
# ==========================================================

def is_super_admin(user=None):
    """
    Returns True if the user is a Super Admin.
    """
    user = user or current_user
    return user.is_authenticated and user.is_super_admin


def is_school_admin(user=None):
    """
    Returns True if the user is a School Admin.
    """
    user = user or current_user
    return user.is_authenticated and user.is_school_admin


def is_teacher(user=None):
    """
    Returns True if the user is a Teacher.
    """
    user = user or current_user
    return user.is_authenticated and user.is_teacher


def is_parent(user=None):
    """
    Returns True if the user is a Parent.
    """
    user = user or current_user
    return user.is_authenticated and user.is_parent


# ==========================================================
# STUDENT PERMISSIONS
# ==========================================================

def can_view_students(user=None):
    user = user or current_user
    return (
        is_super_admin(user)
        or is_school_admin(user)
        or is_teacher(user)
    )


def can_create_student(user=None):
    user = user or current_user
    return (
        is_super_admin(user)
        or is_school_admin(user)
    )


def can_edit_student(user=None):
    user = user or current_user
    return (
        is_super_admin(user)
        or is_school_admin(user)
    )


def can_delete_student(user=None):
    user = user or current_user
    return (
        is_super_admin(user)
        or is_school_admin(user)
    )


# ==========================================================
# TEACHER PERMISSIONS
# ==========================================================

def can_manage_teachers(user=None):
    user = user or current_user
    return (
        is_super_admin(user)
        or is_school_admin(user)
    )


# ==========================================================
# PARENT PERMISSIONS
# ==========================================================

def can_manage_parents(user=None):
    user = user or current_user
    return (
        is_super_admin(user)
        or is_school_admin(user)
    )


# ==========================================================
# CLASSROOM PERMISSIONS
# ==========================================================

def can_manage_classrooms(user=None):
    user = user or current_user
    return (
        is_super_admin(user)
        or is_school_admin(user)
    )


# ==========================================================
# BEHAVIOUR PERMISSIONS
# ==========================================================

def can_record_behaviour(user=None):
    user = user or current_user
    return (
        is_teacher(user)
        or is_school_admin(user)
    )


def can_edit_behaviour(user=None):
    user = user or current_user
    return (
        is_teacher(user)
        or is_school_admin(user)
    )


def can_delete_behaviour(user=None):
    user = user or current_user
    return (
        is_school_admin(user)
        or is_super_admin(user)
    )


# ==========================================================
# ATTENDANCE PERMISSIONS
# ==========================================================

def can_take_attendance(user=None):
    user = user or current_user
    return (
        is_teacher(user)
        or is_school_admin(user)
    )


# ==========================================================
# ACADEMIC RECORD PERMISSIONS
# ==========================================================

def can_enter_scores(user=None):
    user = user or current_user
    return (
        is_teacher(user)
        or is_school_admin(user)
    )


# ==========================================================
# REPORT PERMISSIONS
# ==========================================================

def can_generate_reports(user=None):
    user = user or current_user
    return (
        is_school_admin(user)
        or is_super_admin(user)
    )


# ==========================================================
# SCHOOL SETTINGS
# ==========================================================

def can_manage_school(user=None):
    user = user or current_user
    return (
        is_school_admin(user)
        or is_super_admin(user)
    )