from flask import url_for


def get_dashboard_url(user):
    """
    Returns the correct dashboard endpoint
    based on the authenticated user's role.
    """

    if user.is_super_admin:
        return url_for("super_admin.dashboard")

    elif user.is_school_admin:
        return url_for("school_admin.dashboard")

    elif user.is_teacher:
        return url_for("teacher.dashboard")

    elif user.is_parent:
        return url_for("parent.dashboard")

    return url_for("auth.login")