"""
=========================================================
Activity Logging Helper
=========================================================
"""

from packages.extensions import db
from packages.models.activity import Activity
from flask_login import current_user


def log_activity(
    action,
    description,
    entity_type=None,
    entity_id=None,
    icon=None,
    school_id=None,
    user_id=None
):
    

    # -----------------------------------------------------
    # GET SCHOOL FROM CURRENT USER
    # -----------------------------------------------------

    if school_id is None:

        if (
            current_user.is_authenticated
            and hasattr(current_user, "school_id")
        ):
            school_id = current_user.school_id

    # -----------------------------------------------------
    # GET USER FROM CURRENT USER
    # -----------------------------------------------------

    if user_id is None:

        if current_user.is_authenticated:

            user_id = current_user.id

    # -----------------------------------------------------
    # CREATE ACTIVITY
    # -----------------------------------------------------

    activity = Activity(
        school_id=school_id,
        user_id=user_id,
        action=action,
        description=description,
        entity_type=entity_type,
        entity_id=entity_id,
        icon=icon
    )

    # -----------------------------------------------------
    # ADD TO DATABASE
    # -----------------------------------------------------

    db.session.add(activity)

    return activity