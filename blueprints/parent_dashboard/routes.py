from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from packages.models.student import Student
from packages.models.parent import Parent
from packages.models.attendance import Attendance
from . import parent_dash_bp
from packages.extensions import db
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

    # Temporary child data
    child = {
        "id": 1,
        "name": "David James",
        "class_name": "JSS 2A",
        "avatar": None
    }

    # Summary cards
    summary = {
        "present": 82,
        "late": 4,
        "absent": 3,
        "rate": 92
    }

    # Percentage breakdown
    breakdown = {
        "present": 92,
        "late": 5,
        "absent": 3
    }

    # Monthly trend
    monthly_trend = [
        {"month": "February", "rate": 94},
        {"month": "March", "rate": 91},
        {"month": "April", "rate": 95},
        {"month": "May", "rate": 89},
        {"month": "June", "rate": 93},
        {"month": "July", "rate": 92},
    ]

    # Recent attendance records
    records = [
        {
            "date": "31 Jul 2026",
            "status": "present",
            "time": "7:45 AM"
        },
        {
            "date": "30 Jul 2026",
            "status": "late",
            "time": "8:12 AM"
        },
        {
            "date": "29 Jul 2026",
            "status": "present",
            "time": "7:48 AM"
        },
        {
            "date": "28 Jul 2026",
            "status": "absent",
            "time": None
        },
        {
            "date": "27 Jul 2026",
            "status": "present",
            "time": "7:50 AM"
        }
    ]

    return render_template(
        "parent_dash/attendance/home.html",
        child=child,
        summary=summary,
        breakdown=breakdown,
        monthly_trend=monthly_trend,
        records=records
    )
        
        
    

# ==========================================================
# ATTENDANCE HISTORY
# ==========================================================

@parent_dash_bp.route("/attendance/history", endpoint="attendance_history")
def attendance_history():

    # Temporary child data
    child = {
        "id": 1,
        "name": "David James",
        "class_name": "JSS 2A",
        "avatar": None
    }

    # Filter values
    filters = {
        "from_date": "2026-07-01",
        "to_date": "2026-07-31"
    }

    # Summary statistics
    stats = {
        "total_days": 89,
        "present": 82,
        "late": 4,
        "absent": 3
    }

    # Attendance records
    records = [
        {
            "date": "31 Jul 2026",
            "day": "Friday",
            "status": "present",
            "time": "7:45 AM",
            "remark": "On time"
        },
        {
            "date": "30 Jul 2026",
            "day": "Thursday",
            "status": "late",
            "time": "8:12 AM",
            "remark": "Traffic delay"
        },
        {
            "date": "29 Jul 2026",
            "day": "Wednesday",
            "status": "present",
            "time": "7:48 AM",
            "remark": "On time"
        },
        {
            "date": "28 Jul 2026",
            "day": "Tuesday",
            "status": "absent",
            "time": None,
            "remark": "Medical leave"
        },
        {
            "date": "27 Jul 2026",
            "day": "Monday",
            "status": "present",
            "time": "7:50 AM",
            "remark": "On time"
        },
        {
            "date": "24 Jul 2026",
            "day": "Friday",
            "status": "present",
            "time": "7:43 AM",
            "remark": "Excellent punctuality"
        },
        {
            "date": "23 Jul 2026",
            "day": "Thursday",
            "status": "present",
            "time": "7:46 AM",
            "remark": "On time"
        },
        {
            "date": "22 Jul 2026",
            "day": "Wednesday",
            "status": "late",
            "time": "8:05 AM",
            "remark": "Heavy rain"
        }
    ]

    return render_template(
        "parent_dash/attendance/history.html",
        child=child,
        filters=filters,
        stats=stats,
        records=records
    )


# ==========================================================
# ACADEMICS HOME
# ==========================================================

@parent_dash_bp.route("/academics", endpoint="academics_home")
def academics_home():

    child = {
        "id": 1,
        "name": "David James",
        "class_name": "JSS 2A",
        "avatar": None
    }

    current_term = "Third Term 2025/2026"

    summary = {
        "average": 78,
        "position": "5th",
        "passed": 8,
        "total_subjects": 9,
        "best_subject": "ICT"
    }

    subjects = [
        {"name": "Mathematics", "ca": "18/20", "exam": "64/80", "total": 82},
        {"name": "English", "ca": "16/20", "exam": "60/80", "total": 76},
        {"name": "Basic Science", "ca": "19/20", "exam": "69/80", "total": 88},
        {"name": "Social Studies", "ca": "17/20", "exam": "55/80", "total": 72},
        {"name": "ICT", "ca": "20/20", "exam": "71/80", "total": 91},
    ]

    term_comparison = [
        {"term": "First Term", "session": "2025/2026", "average": 74},
        {"term": "Second Term", "session": "2025/2026", "average": 76},
        {"term": "Third Term", "session": "2025/2026", "average": 78},
    ]

    teacher_comment = {
        "teacher": "Mrs. A. Johnson",
        "subject": "Class Teacher",
        "comment": "David has shown consistent improvement across most subjects, especially in ICT and Basic Science. Continued focus on English comprehension will further improve overall performance."
    }

    activities = [
        {
            "icon": "bi bi-journal-check",
            "title": "Mathematics test graded",
            "time": "2 hours ago",
            "score": "82%"
        },
        {
            "icon": "bi bi-file-earmark-text",
            "title": "English assignment submitted",
            "time": "Yesterday",
            "score": None
        },
        {
            "icon": "bi bi-award",
            "title": "ICT practical result published",
            "time": "2 days ago",
            "score": "91%"
        }
    ]

    return render_template(
        "parent_dash/academics/home.html",
        child=child,
        current_term=current_term,
        summary=summary,
        subjects=subjects,
        term_comparison=term_comparison,
        teacher_comment=teacher_comment,
        activities=activities
    )


# ==========================================================
# ACADEMICS RESULTS
# ==========================================================

@parent_dash_bp.route("/academics/results", endpoint="academics_results")
def academics_results():

    child = {
        "id": 1,
        "name": "David James",
        "class_name": "JSS 2A",
        "avatar": None
    }

    current_term = "Third Term 2025/2026"

    summary = {
        "average": 78,
        "position": "5th",
        "passed": 8,
        "total_subjects": 9,
        "best_subject": "ICT",
        "below_50": 1
    }

    subjects = [
        {"name": "Mathematics", "ca": 18, "exam": 64, "total": 82, "grade": "A"},
        {"name": "English", "ca": 16, "exam": 60, "total": 76, "grade": "B"},
        {"name": "Basic Science", "ca": 19, "exam": 69, "total": 88, "grade": "A"},
        {"name": "Social Studies", "ca": 17, "exam": 55, "total": 72, "grade": "B"},
        {"name": "ICT", "ca": 20, "exam": 71, "total": 91, "grade": "A"},
        {"name": "Civic Education", "ca": 15, "exam": 50, "total": 65, "grade": "C"},
        {"name": "Business Studies", "ca": 14, "exam": 48, "total": 62, "grade": "C"},
        {"name": "Agricultural Science", "ca": 18, "exam": 58, "total": 76, "grade": "B"},
        {"name": "French", "ca": 10, "exam": 32, "total": 42, "grade": "F"},
    ]

    strongest = max(subjects, key=lambda s: s["total"])
    weakest = min(subjects, key=lambda s: s["total"])

    insight = (
        "David demonstrates strong analytical and technology-related skills, "
        "with excellent performance in ICT and Basic Science. Additional support "
        "in French and language development will help improve overall performance."
    )

    return render_template(
        "parent_dash/academics/results.html",
        child=child,
        current_term=current_term,
        summary=summary,
        subjects=subjects,
        strongest=strongest,
        weakest=weakest,
        insight=insight
    )


# ==========================================================
# BEHAVIOUR HOME
# ==========================================================

@parent_dash_bp.route("/behaviour", endpoint="behaviour_home")
def behaviour_home():

    child = {
        "id": 1,
        "name": "David James",
        "class_name": "JSS 2A",
        "avatar": None
    }

    summary = {
        "positive": 14,
        "concerns": 2,
        "score": 8.5,
        "rating": "Very Good"
    }

    breakdown = [
        {"label": "Respect", "score": 9},
        {"label": "Punctuality", "score": 8},
        {"label": "Teamwork", "score": 9},
        {"label": "Class Participation", "score": 8},
        {"label": "Responsibility", "score": 8},
    ]

    records = [
        {
            "type": "positive",
            "title": "Excellent Teamwork",
            "date": "31 Jul 2026",
            "teacher": "Mrs. Johnson",
            "note": "Worked cooperatively with classmates during the science project."
        },
        {
            "type": "positive",
            "title": "Active Participation",
            "date": "29 Jul 2026",
            "teacher": "Mr. Adeyemi",
            "note": "Contributed confidently during mathematics discussion."
        },
        {
            "type": "concern",
            "title": "Late Arrival",
            "date": "24 Jul 2026",
            "teacher": "Mrs. Johnson",
            "note": "Arrived after assembly and missed the opening activity."
        }
    ]

    teacher_comment = {
        "teacher": "Mrs. A. Johnson",
        "role": "Class Teacher",
        "comment": (
            "David is generally respectful, cooperative, and eager to learn. "
            "He responds well to guidance and continues to show improvement in "
            "class participation and responsibility."
        )
    }

    strengths = [
        "Respects teachers and classmates",
        "Works well in groups",
        "Shows willingness to help others",
        "Participates actively in lessons"
    ]

    growth_areas = [
        "Improve punctuality on some mornings",
        "Maintain focus during extended activities"
    ]

    return render_template(
        "parent_dash/behaviour/home.html",
        child=child,
        summary=summary,
        breakdown=breakdown,
        records=records,
        teacher_comment=teacher_comment,
        strengths=strengths,
        growth_areas=growth_areas
    )


# ==========================================================
# REPORT CARDS HOME
# ==========================================================

@parent_dash_bp.route("/report-cards", endpoint="report_cards_home")
def report_cards_home():

    child = {
        "id": 1,
        "name": "David James",
        "class_name": "JSS 2A",
        "avatar": None
    }

    terms = [
        {"name": "Third Term 2025/2026", "current": True},
        {"name": "Second Term 2025/2026", "current": False},
        {"name": "First Term 2025/2026", "current": False},
    ]

    current_term = "Third Term 2025/2026"
    session_name = "2025/2026"

    report = {
        "average": 78,
        "position": "5th of 42",
        "grade": "B+",
        "attendance": 92
    }

    subjects = [
        {"name": "Mathematics", "ca": 18, "exam": 64, "total": 82, "grade": "A"},
        {"name": "English", "ca": 16, "exam": 60, "total": 76, "grade": "B"},
        {"name": "Basic Science", "ca": 19, "exam": 69, "total": 88, "grade": "A"},
        {"name": "Social Studies", "ca": 17, "exam": 55, "total": 72, "grade": "B"},
        {"name": "ICT", "ca": 20, "exam": 71, "total": 91, "grade": "A"},
        {"name": "French", "ca": 10, "exam": 32, "total": 42, "grade": "F"},
    ]

    teacher_comment = {
        "teacher": "Mrs. A. Johnson",
        "role": "Class Teacher",
        "comment": (
            "David has maintained a commendable academic record this term. "
            "He demonstrates strong analytical skills and shows enthusiasm in class activities. "
            "Continued attention to language subjects will further enhance his overall performance."
        )
    }

    principal_comment = {
        "name": "Dr. M. Okafor",
        "comment": (
            "A promising student with good potential. Keep up the hard work, "
            "discipline, and consistent effort in all subjects."
        )
    }

    return render_template(
        "parent_dash/report_cards/home.html",
        child=child,
        terms=terms,
        current_term=current_term,
        session_name=session_name,
        report=report,
        subjects=subjects,
        teacher_comment=teacher_comment,
        principal_comment=principal_comment
    )


# ==========================================================
# NOTIFICATIONS HOME
# ==========================================================

@parent_dash_bp.route("/notifications", endpoint="notifications_home")
def notifications_home():

    notifications = [
        {
            "type": "attendance",
            "icon": "bi-calendar-check-fill",
            "title": "Attendance recorded",
            "time": "Today · 7:55 AM",
            "message": "David James was marked present for school today.",
            "read": False,
            "action_url": url_for("parent_dashboard.attendance_home"),
            "action_text": "View Attendance"
        },
        {
            "type": "academic",
            "icon": "bi-journal-check",
            "title": "Mathematics test graded",
            "time": "Today · 1:20 PM",
            "message": "A new Mathematics test score of 82% has been published.",
            "read": False,
            "action_url": url_for("parent_dashboard.academics_results"),
            "action_text": "View Result"
        },
        {
            "type": "announcement",
            "icon": "bi-megaphone-fill",
            "title": "PTA meeting reminder",
            "time": "Yesterday · 5:00 PM",
            "message": "The PTA meeting will hold on Friday at 4:00 PM in the school hall.",
            "read": True,
            "action_url": None
        },
        {
            "type": "behaviour",
            "icon": "bi-award-fill",
            "title": "Positive behaviour note",
            "time": "2 days ago",
            "message": "David received a commendation for excellent teamwork during a group activity.",
            "read": True,
            "action_url": url_for("parent_dashboard.behaviour_home"),
            "action_text": "View Behaviour"
        },
        {
            "type": "academic",
            "icon": "bi-file-earmark-text",
            "title": "Report card available",
            "time": "3 days ago",
            "message": "Third Term report card is now available for download.",
            "read": True,
            "action_url": url_for("parent_dashboard.report_cards_home"),
            "action_text": "Open Report"
        }
    ]

    return render_template(
        "parent_dash/notifications/home.html",
        notifications=notifications
    )


# ==========================================================
# PROFILE HOME
# ==========================================================

@parent_dash_bp.route("/profile", endpoint="profile")
def profile():

    parent = {
        "name": "Mr. Michael James",
        "email": "michael.james@example.com",
        "phone": "+234 801 234 5678",
        "relationship": "Father",
        "address": "15 Unity Avenue, Ikeja, Lagos",
        "children_count": 2,
        "joined": "Jan 2026",
        "avatar": None
    }

    children = [
        {
            "id": 1,
            "name": "David James",
            "class_name": "JSS 2A",
            "avatar": None
        },
        {
            "id": 2,
            "name": "Sarah James",
            "class_name": "Primary 5B",
            "avatar": None
        }
    ]

    notification_settings = [
        {
            "label": "Attendance Alerts",
            "description": "Receive notifications when a child is absent or late.",
            "enabled": True
        },
        {
            "label": "Academic Updates",
            "description": "New results, assignments, and report cards.",
            "enabled": True
        },
        {
            "label": "Behaviour Notifications",
            "description": "Positive notes and behaviour concerns.",
            "enabled": True
        },
        {
            "label": "School Announcements",
            "description": "Events, meetings, and important notices.",
            "enabled": False
        }
    ]

    return render_template(
        "parent_dash/profile/home.html",
        parent=parent,
        children=children,
        notification_settings=notification_settings
    )

# ==========================================================
# PROFILE EDIT
# ==========================================================

@parent_dash_bp.route("/profile/edit", methods=["GET", "POST"], endpoint="edit_profile")
def edit_profile():

    parent = {
        "name": "Michael James",
        "first_name": "Michael",
        "last_name": "James",
        "email": "michael.james@example.com",
        "phone": "+234 801 234 5678",
        "relationship": "Father",
        "occupation": "Software Engineer",
        "address": "15 Unity Avenue, Ikeja",
        "city": "Lagos",
        "state": "Lagos",
        "country": "Nigeria",
        "emergency_name": "Mary James",
        "emergency_phone": "+234 809 876 5432",
        "avatar": None
    }

    if request.method == "POST":
        flash("Profile updated successfully.", "success")
        return redirect(url_for("parent_dashboard.profile_home"))

    return render_template(
        "parent_dash/profile/edit.html",
        parent=parent
    )
    
# ==========================================================
# PROFILE SECURITY
# ==========================================================

@parent_dash_bp.route("/profile/security", methods=["GET", "POST"], endpoint="profile_security")
def profile_security():

    if request.method == "POST":
        flash("Password updated successfully.", "success")
        return redirect(url_for("parent_dashboard.profile_security"))

    sessions = [
        {
            "device": "Windows PC · Chrome",
            "location": "Lagos, Nigeria",
            "last_active": "Active now",
            "current": True
        },
        {
            "device": "Android Phone · Chrome",
            "location": "Lagos, Nigeria",
            "last_active": "Yesterday at 8:42 PM",
            "current": False
        },
        {
            "device": "iPad · Safari",
            "location": "Abuja, Nigeria",
            "last_active": "3 days ago",
            "current": False
        }
    ]

    return render_template(
        "parent_dash/profile/security.html",
        sessions=sessions
    )

# ==========================================================
# SETTINGS
# ==========================================================

@parent_dash_bp.route("/settings", endpoint="settings")
def settings():
    return render_template("parent_dash/settings/home.html")