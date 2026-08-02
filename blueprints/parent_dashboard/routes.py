from flask import render_template
from flask_login import login_required, current_user
from packages.models.student import Student
from packages.models.parent import Parent
from packages.models.attendance import Attendance
from . import parent_dash_bp
# ==========================================================
# PARENT DASHBOARD
# ==========================================================

@parent_dash_bp.route("/", endpoint="parent_dashboard")
def parent_dashboard():

    # Demo / placeholder data
    alerts = [
        {
            "category": "warning",
            "icon": "bi bi-exclamation-triangle-fill",
            "title": "Low Attendance Alert",
            "message": "David James has missed 3 classes this week.",
            "url": "#"
        },
        {
            "category": "info",
            "icon": "bi bi-info-circle-fill",
            "title": "New Report Card Available",
            "message": "Third term report card is ready for download.",
            "url": "#"
        }
    ]

    children = [
        {
            "id": 1,
            "name": "David James",
            "class_name": "JSS 2A",
            "attendance": 92,
            "average": 78,
            "behaviour": "Good",
            "avatar": None
        },
        {
            "id": 2,
            "name": "Sarah James",
            "class_name": "Primary 5",
            "attendance": 96,
            "average": 84,
            "behaviour": "Excellent",
            "avatar": None
        }
    ]

    attendance = {
        "present": 92,
        "late": 5,
        "absent": 3
    }

    subjects = [
        {"name": "Mathematics", "score": 82},
        {"name": "English", "score": 76},
        {"name": "Basic Science", "score": 88},
        {"name": "ICT", "score": 91}
    ]

    behaviour_records = [
        {
            "type": "positive",
            "title": "Excellent Participation",
            "date": "28 Jul 2026",
            "note": "Actively contributed during class discussion."
        },
        {
            "type": "warning",
            "title": "Homework Reminder",
            "date": "26 Jul 2026",
            "note": "Homework submitted late."
        }
    ]

    events = [
        {"day": "02", "month": "AUG", "title": "Parents Meeting", "time": "10:00 AM"},
        {"day": "05", "month": "AUG", "title": "Mathematics Test", "time": "9:00 AM"},
        {"day": "08", "month": "AUG", "title": "Sports Day", "time": "8:00 AM"}
    ]

    notifications = [
        {
            "type": "academic",
            "icon": "bi bi-book-fill",
            "title": "Mathematics Result Published",
            "message": "David scored 82% in Mathematics.",
            "time": "1h ago"
        },
        {
            "type": "attendance",
            "icon": "bi bi-calendar-check-fill",
            "title": "Attendance Updated",
            "message": "Attendance for today has been recorded.",
            "time": "3h ago"
        },
        {
            "type": "event",
            "icon": "bi bi-calendar-event-fill",
            "title": "Upcoming Parents Meeting",
            "message": "Parents meeting scheduled for 2 Aug 2026.",
            "time": "Yesterday"
        }
    ]

    return render_template(
        "parent_dash/parent_dashboard.html",
        
        alerts=alerts,
        children=children,
        attendance=attendance,
        subjects=subjects,
        behaviour_records=behaviour_records,
        events=events,
        notifications=notifications
    )


# ==========================================================
# CHILDREN
# ==========================================================

@parent_dash_bp.route("/children", endpoint="children_home")
def children_home():
    return render_template("parent_dash/children/home.html")


@parent_dash_bp.route("/children/<int:id>", endpoint="child_profile")
def child_profile(id):

    # Temporary demo data
    child = {
        "id": id,
        "name": "David James",
        "class_name": "JSS 2A",
        "admission_no": "RI-2026-001",
        "attendance": 92,
        "average": 78,
        "behaviour": "Good",
        "position": "5th",
        "gender": "Male",
        "dob": "12 Mar 2013",
        "session": "2025/2026",
        "status": "active",
        "last_update": "2 hours ago",
        "avatar": None
    }

    attendance = {
        "present": 92,
        "late": 5,
        "absent": 3
    }

    subjects = [
        {"name": "Mathematics", "score": 82},
        {"name": "English", "score": 76},
        {"name": "Basic Science", "score": 88},
        {"name": "ICT", "score": 91}
    ]

    behaviour_records = [
        {
            "type": "positive",
            "title": "Excellent Participation",
            "date": "28 Jul 2026",
            "note": "Actively contributed during class discussion."
        }
    ]

    activities = [
        {
            "icon": "bi bi-book-fill",
            "title": "Mathematics result updated",
            "time": "1 hour ago"
        }
    ]

    return render_template(
        "parent_dash/children/profile.html",
        child=child,
        attendance=attendance,
        subjects=subjects,
        behaviour_records=behaviour_records,
        activities=activities
    )                


# ==========================================================
# ATTENDANCE
# ==========================================================

@parent_dash_bp.route("/attendance", endpoint="attendance_home")
def attendance_home():

    child = Student.query.get_or_404(id)

    records = (
        Attendance.query
        .filter_by(student_id=child.id)
        .order_by(Attendance.date.desc())
        .all()
    )

    return render_template(
        "parent_dash/attendance/home.html",
        child=child,
        records=records
        
    )

@parent_dash_bp.route("/attendance/history", endpoint="attendance_history")
def attendance_history():
    return render_template("parent_dash/attendance/history.html")


# ==========================================================
# ACADEMICS
# ==========================================================

@parent_dash_bp.route("/academics", endpoint="academics_home")
def academics_home():
    return render_template("parent_dash/academics/home.html")


@parent_dash_bp.route("/academics/results", endpoint="academics_results")
def academics_results():
    return render_template("parent_dash/academics/results.html")


# ==========================================================
# BEHAVIOUR
# ==========================================================

@parent_dash_bp.route("/behaviour", endpoint="behaviour_home")
def behaviour_home():
    return render_template("parent_dash/behaviour/home.html")


# ==========================================================
# REPORT CARDS
# ==========================================================

@parent_dash_bp.route("/report-cards", endpoint="report_cards_home")
def report_cards_home():
    return render_template("parent_dash/report_cards/home.html")


# ==========================================================
# NOTIFICATIONS
# ==========================================================

@parent_dash_bp.route("/notifications", endpoint="notifications_home")
def notifications_home():
    return render_template("parent_dash/notifications/home.html")


# ==========================================================
# PROFILE
# ==========================================================

@parent_dash_bp.route("/profile", endpoint="profile")
def profile():
    return render_template("parent_dash/profile/home.html")


# ==========================================================
# SETTINGS
# ==========================================================

@parent_dash_bp.route("/settings", endpoint="settings")
def settings():
    return render_template("parent_dash/settings/home.html")