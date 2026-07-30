from flask import render_template

from blueprints.attendance.services import attendance_summary

from . import parent_bp


# ==========================================================
# PARENT DASHBOARD
# ==========================================================

@parent_bp.route("/", endpoint="parent_dashboard")
def parent_dashboard():
    return render_template("parent_dash/parent_dashboard.html")


# ==========================================================
# CHILDREN
# ==========================================================

@parent_bp.route("/children<int:student_id>", endpoint="parent_children")
def parent_child():
    return render_template("children/home.html")


@parent_bp.route("/children/profile")
def child_profile():
    return render_template("children/profile.html")


# ==========================================================
# ATTENDANCE
# ==========================================================

@parent_bp.route("/attendance")
def attendance():
    return render_template("attendance/home.html")


# ==========================================================
# ACADEMICS
# ==========================================================

@parent_bp.route("/academics")
def academics():
    return render_template("academics/home.html")


@parent_bp.route("/academics/results")
def results():
    return render_template("academics/results.html")


@parent_bp.route("/academics/subject-analysis")
def subject_analysis():
    return render_template("academics/subject_analysis.html")


# ==========================================================
# BEHAVIOUR
# ==========================================================

@parent_bp.route("/behaviour")
def behaviour():
    return render_template("behaviour/home.html")


# ==========================================================
# REPORT CARDS
# ==========================================================

@parent_bp.route("/report-cards")
def report_cards():
    return render_template("report_cards/home.html")


# ==========================================================
# NOTIFICATIONS
# ==========================================================

@parent_bp.route("/notifications")
def notifications():
    return render_template("notifications/home.html")


# ==========================================================
# PROFILE
# ==========================================================

@parent_bp.route("/profile")
def profile():
    return render_template("profile/home.html")


# ==========================================================
# SETTINGS
# ==========================================================

@parent_bp.route("/settings")
def settings():
    return render_template("settings/home.html")