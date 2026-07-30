"""
=========================================================
Super Admin Permissions
=========================================================

Defines permissions available to the Super
Administrator module.

These permissions can later be stored in the
database and assigned to roles.
"""

# ==========================================================
# DASHBOARD
# ==========================================================

VIEW_DASHBOARD = "view_dashboard"


# ==========================================================
# SCHOOL MANAGEMENT
# ==========================================================

VIEW_SCHOOLS = "view_schools"

CREATE_SCHOOL = "create_school"

EDIT_SCHOOL = "edit_school"

DELETE_SCHOOL = "delete_school"

APPROVE_SCHOOL = "approve_school"


# ==========================================================
# USER MANAGEMENT
# ==========================================================

VIEW_USERS = "view_users"

CREATE_USER = "create_user"

EDIT_USER = "edit_user"

DELETE_USER = "delete_user"

LOCK_USER = "lock_user"

UNLOCK_USER = "unlock_user"

ACTIVATE_USER = "activate_user"

DEACTIVATE_USER = "deactivate_user"


# ==========================================================
# ROLE MANAGEMENT
# ==========================================================

VIEW_ROLES = "view_roles"

CREATE_ROLE = "create_role"

EDIT_ROLE = "edit_role"

DELETE_ROLE = "delete_role"


# ==========================================================
# REPORTS
# ==========================================================

VIEW_REPORTS = "view_reports"

EXPORT_REPORTS = "export_reports"


# ==========================================================
# NOTIFICATIONS
# ==========================================================

VIEW_NOTIFICATIONS = "view_notifications"

SEND_NOTIFICATION = "send_notification"


# ==========================================================
# AUDIT LOGS
# ==========================================================

VIEW_AUDIT_LOGS = "view_audit_logs"


# ==========================================================
# SYSTEM SETTINGS
# ==========================================================

VIEW_SETTINGS = "view_settings"

EDIT_SETTINGS = "edit_settings"


# ==========================================================
# SECURITY
# ==========================================================

VIEW_SECURITY = "view_security"

MANAGE_SECURITY = "manage_security"


# ==========================================================
# SUBSCRIPTIONS
# ==========================================================

VIEW_SUBSCRIPTIONS = "view_subscriptions"

MANAGE_SUBSCRIPTIONS = "manage_subscriptions"


# ==========================================================
# PAYMENTS
# ==========================================================

VIEW_PAYMENTS = "view_payments"

MANAGE_PAYMENTS = "manage_payments"


# ==========================================================
# BACKUPS
# ==========================================================

CREATE_BACKUP = "create_backup"

RESTORE_BACKUP = "restore_backup"


# ==========================================================
# SYSTEM MAINTENANCE
# ==========================================================

VIEW_SYSTEM = "view_system"

MAINTENANCE_MODE = "maintenance_mode"


# ==========================================================
# ALL SUPER ADMIN PERMISSIONS
# ==========================================================

SUPERADMIN_PERMISSIONS = {

    VIEW_DASHBOARD,

    VIEW_SCHOOLS,
    CREATE_SCHOOL,
    EDIT_SCHOOL,
    DELETE_SCHOOL,
    APPROVE_SCHOOL,

    VIEW_USERS,
    CREATE_USER,
    EDIT_USER,
    DELETE_USER,
    LOCK_USER,
    UNLOCK_USER,
    ACTIVATE_USER,
    DEACTIVATE_USER,

    VIEW_ROLES,
    CREATE_ROLE,
    EDIT_ROLE,
    DELETE_ROLE,

    VIEW_REPORTS,
    EXPORT_REPORTS,

    VIEW_NOTIFICATIONS,
    SEND_NOTIFICATION,

    VIEW_AUDIT_LOGS,

    VIEW_SETTINGS,
    EDIT_SETTINGS,

    VIEW_SECURITY,
    MANAGE_SECURITY,

    VIEW_SUBSCRIPTIONS,
    MANAGE_SUBSCRIPTIONS,

    VIEW_PAYMENTS,
    MANAGE_PAYMENTS,

    CREATE_BACKUP,
    RESTORE_BACKUP,

    VIEW_SYSTEM,
    MAINTENANCE_MODE
}


# ==========================================================
# PERMISSION CHECK
# ==========================================================

def has_permission(user, permission):
    """
    Check whether a user has a permission.

    Currently, every Super Admin has every permission.

    Later this can be replaced with database-driven
    permissions.
    """

    if not user:
        return False

    if not getattr(user, "is_super_admin", False):
        return False

    return permission in SUPERADMIN_PERMISSIONS


# ==========================================================
# MULTIPLE PERMISSIONS
# ==========================================================

def has_permissions(user, permissions):
    """
    Check multiple permissions.
    """

    return all(
        has_permission(user, permission)
        for permission in permissions
    )


# ==========================================================
# ANY PERMISSION
# ==========================================================

def has_any_permission(user, permissions):
    """
    Check whether the user has at least
    one permission.
    """

    return any(
        has_permission(user, permission)
        for permission in permissions
    )