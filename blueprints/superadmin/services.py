"""
=========================================================
Super Admin Services
=========================================================

Business logic for the Super Administrator module.
"""

from datetime import datetime

from sqlalchemy import func

from packages.extensions import db

from packages.models import (
    School,
    User,
    Teacher,
    Parent,
    Student,
    Role
)


# ==========================================================
# DASHBOARD STATISTICS
# ==========================================================

def get_dashboard_statistics():
    """
    Returns statistics displayed on the dashboard.
    """

    return {

        "schools": School.query.count(),

        "users": User.query.count(),

        "teachers": Teacher.query.count(),

        "students": Student.query.count(),

        "parents": Parent.query.count(),

        "active_users":
            User.query.filter_by(
                is_active=True
            ).count()

    }


# ==========================================================
# RECENT SCHOOLS
# ==========================================================

def get_recent_schools(limit=10):

    return School.query.order_by(

        School.created_at.desc()

    ).limit(limit).all()


# ==========================================================
# RECENT USERS
# ==========================================================

def get_recent_users(limit=10):

    return User.query.order_by(

        User.created_at.desc()

    ).limit(limit).all()


# ==========================================================
# FIND SCHOOL
# ==========================================================

def get_school(school_id):

    return School.query.get_or_404(school_id)


# ==========================================================
# FIND USER
# ==========================================================

def get_user(user_id):

    return User.query.get_or_404(user_id)


# ==========================================================
# ACTIVATE USER
# ==========================================================

def activate_user(user):

    user.is_active = True

    db.session.commit()

    return True


# ==========================================================
# DEACTIVATE USER
# ==========================================================

def deactivate_user(user):

    user.is_active = False

    db.session.commit()

    return True


# ==========================================================
# LOCK USER
# ==========================================================

def lock_user(user):

    user.is_locked = True

    db.session.commit()

    return True


# ==========================================================
# UNLOCK USER
# ==========================================================

def unlock_user(user):

    user.is_locked = False

    user.failed_login_attempts = 0

    db.session.commit()

    return True


# ==========================================================
# DELETE USER
# ==========================================================

def delete_user(user):

    db.session.delete(user)

    db.session.commit()

    return True


# ==========================================================
# SAVE PLATFORM SETTINGS
# ==========================================================

def save_platform_settings(form):

    """
    Placeholder until SystemSettings model exists.
    """

    # TODO

    return True


# ==========================================================
# GET PLATFORM SETTINGS
# ==========================================================

def get_platform_settings():

    """
    Placeholder.

    Replace with SystemSettings model later.
    """

    return {}


# ==========================================================
# RECENT NOTIFICATIONS
# ==========================================================

def get_recent_notifications(limit=20):

    """
    Placeholder.
    """

    return []


# ==========================================================
# RECENT AUDIT LOGS
# ==========================================================

def get_recent_audit_logs(limit=50):

    """
    Placeholder.
    """

    return []


# ==========================================================
# SYSTEM HEALTH
# ==========================================================

def get_system_health():

    return {

        "database": "Online",

        "storage": "Healthy",

        "server": "Running",

        "timestamp": datetime.utcnow()

    }


# ==========================================================
# GLOBAL SEARCH
# ==========================================================

def search(keyword):

    schools = School.query.filter(

        School.name.ilike(f"%{keyword}%")

    ).all()

    users = User.query.filter(

        User.username.ilike(f"%{keyword}%")

    ).all()

    return {

        "schools": schools,

        "users": users

    }


# ==========================================================
# USER COUNTS BY ROLE
# ==========================================================

def get_user_role_statistics():

    results = (

        db.session.query(

            Role.name,

            func.count(User.id)

        )

        .join(User)

        .group_by(Role.name)

        .all()

    )

    return results


# ==========================================================
# DASHBOARD CHART DATA
# ==========================================================

def dashboard_chart_data():

    return {

        "schools": School.query.count(),

        "students": Student.query.count(),

        "teachers": Teacher.query.count(),

        "parents": Parent.query.count()

    }