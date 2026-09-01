from flask import render_template, url_for, abort
from flask_login import login_required, current_user
from datetime import date, datetime, timedelta
from sqlalchemy import func


from packages.extensions import db
from packages.models.student import Student
from packages.models.teacher import Teacher
from packages.models.parent import Parent
from packages.models.classroom import Classroom
from packages.models import Attendance
from packages.models import Behaviour
from packages.models import AcademicRecord
from packages.models.activity import Activity

from . import dashboard_bp


# ======================================================
# Dashboard
# ======================================================

@dashboard_bp.route("/", endpoint="dashboard")
@login_required
def dashboard():
    
    
# =====================================================
# SCHOOL ACCESS
# =====================================================
    
    if not current_user.is_school_admin:
            abort(403)
    
    if not current_user.school_id:
            abort(403)
            
    school_id = current_user.school_id
    
    recent_activities = []

# ---------------------------------------------------------
# RECENT STUDENTS
# ---------------------------------------------------------

    students = (
        Student.query
        .filter_by(school_id=school_id)
        .order_by(Student.created_at.desc())
        .limit(5)
        .all()
    )

    for student in students:

        recent_activities.append({
            "message": f"{student.full_name} was registered as a student.",
            "date": student.created_at,
            "icon": "bi bi-person-plus-fill"
        })


# ---------------------------------------------------------
# RECENT TEACHERS
# ---------------------------------------------------------

    teachers = (
        Teacher.query
        .filter_by(school_id=school_id)
        .order_by(Teacher.created_at.desc())
        .limit(5)
        .all()
    )

    for teacher in teachers:

        recent_activities.append({
            "message": f"{teacher.full_name} was added as a teacher.",
            "date": teacher.created_at,
            "icon": "bi bi-person-workspace"
        })


# ---------------------------------------------------------
# RECENT ATTENDANCE
# ---------------------------------------------------------

    attendance_records = (
        Attendance.query
        .filter_by(school_id=school_id)
        .order_by(Attendance.created_at.desc())
        .limit(5)
        .all()
    )

    for attendance in attendance_records:

        recent_activities.append({
            "message": "Student attendance was recorded.",
            "date": attendance.created_at,
            "icon": "bi bi-calendar-check-fill"
        })


# ---------------------------------------------------------
# RECENT ACADEMIC RECORDS
# ---------------------------------------------------------

    academic_records = (
        AcademicRecord.query
        .filter_by(school_id=school_id)
        .order_by(AcademicRecord.created_at.desc())
        .limit(5)
        .all()
    )

    for record in academic_records:

        recent_activities.append({
            "message": "Academic scores were uploaded.",
            "date": record.created_at,
            "icon": "bi bi-bar-chart-fill"
        })


# ---------------------------------------------------------
# RECENT BEHAVIOUR RECORDS
# ---------------------------------------------------------

    behaviour_records = (
        Behaviour.query
        .filter_by(school_id=school_id)
        .order_by(Behaviour.created_at.desc())
        .limit(5)
        .all()
    )

    for behaviour in behaviour_records:

        recent_activities.append({
            "message": "A behaviour report was submitted.",
            "date": behaviour.created_at,
            "icon": "bi bi-emoji-smile-fill"
        })


# ---------------------------------------------------------
# SORT EVERYTHING BY DATE
# ---------------------------------------------------------

    recent_activities = (
        Activity.query
        .filter_by(school_id=school_id)
        .order_by(Activity.created_at.desc())
        .limit(5)
        .all()
    )

# Keep only the five most recent activities
    recent_activities = recent_activities[:5]
    
# =====================================================
# ATTENDANCE CHART
# =====================================================

    attendance_chart_labels = []
    attendance_chart_data = []

    today = date.today()

    # Last 7 days
    for i in range(6, -1, -1):

        current_date = today - timedelta(days=i)

        records = (
            Attendance.query
            .filter(
                Attendance.school_id == school_id,
                Attendance.attendance_date == current_date
            )
            .all()
        )

        total = len(records)

        present = sum(
            1
            for record in records
            if record.status == "Present"
        )

        if total > 0:
            percentage = round(
                (present / total) * 100,
                1
            )
        else:
            percentage = 0

        attendance_chart_labels.append(
            current_date.strftime("%a")
        )

        attendance_chart_data.append(
            percentage
        )


    # =====================================================
    # SCHOOL
    # =====================================================

    school = current_user.school

    # =====================================================
    # STUDENTS
    # =====================================================

    total_students = (
        Student.query
        .filter_by(
            school_id=school_id,
            status="Active"
        )
        .count()
    )

    # =====================================================
    # TEACHERS
    # =====================================================

    total_teachers = (
        Teacher.query
        .filter_by(
            school_id=school_id,
            status="Active"
        )
        .count()
    )

    # =====================================================
    # CLASSROOMS
    # =====================================================

    total_classrooms = (
        Classroom.query
        .filter_by(
            school_id=school_id
        )
        .count()
    )
    
    classrooms = (
    Classroom.query
    .filter_by(school_id=school_id)
    .all()
    )

    # =====================================================
    # TODAY'S ATTENDANCE
    # =====================================================

    today = date.today()

    today_attendance = (
        Attendance.query
        .filter_by(
            school_id=school_id,
            attendance_date=today
        )
        .all()
    )

    total_today_attendance = len(today_attendance)
    
    present_today = sum(
        1
        for record in today_attendance
        if record.status == "Present"
    )

    attendance_percentage = 0

    if today_attendance:

        attendance_percentage = round(
            (present_today / len(today_attendance)) * 100,
            1
        )

    # =====================================================
    # BEHAVIOUR
    # =====================================================

    total_behaviours = (
        Behaviour.query
        .filter_by(
            school_id=school_id
        )
        .count()
    )

    positive_behaviours = (
        Behaviour.query
        .filter_by(
            school_id=school_id,
            behaviour_type="Positive"
        )
        .count()
    )

    negative_behaviours = (
        Behaviour.query
        .filter_by(
            school_id=school_id,
            behaviour_type="Negative"
        )
        .count()
    )

    # =====================================================
    # BEHAVIOUR CASES
    # =====================================================

    behaviour_cases = (
        Behaviour.query
        .filter_by(
            school_id=school_id,
            resolved=False
        )
        .count()
    )
    
    # =====================================================
    # BEHAVIOUR SUMMARY
    # =====================================================

    behaviour_records = (
        Behaviour.query
        .filter(
            Behaviour.school_id == school_id
        )
        .all()
    )

    excellent_behaviours = sum(
        1
        for behaviour in behaviour_records
        if behaviour.behaviour_points >= 5
    )

    good_behaviours = sum(
        1
        for behaviour in behaviour_records
        if 1 <= behaviour.behaviour_points < 5
    )

    needs_attention_behaviours = sum(
        1
        for behaviour in behaviour_records
        if behaviour.behaviour_points <= 0
    )

    # =====================================================
    # ACADEMIC PERFORMANCE
    # =====================================================

    academic_average_score = (
        db.session.query(
            func.avg(AcademicRecord.total_score)
        )
        .filter(
            AcademicRecord.school_id == school_id
        )
        .scalar()
    )

    academic_average_score = round(
        academic_average_score or 0,
        1
    )

    # =====================================================
    # TOP PERFORMING CLASSES
    # =====================================================

    classrooms = (
        Classroom.query
        .filter_by(
            school_id=school_id
        )
        .all()
    )

    top_classes = []

    for classroom in classrooms:

        students = [
            student
            for student in classroom.students
            if student.status == "Active"
        ]

        student_ids = [
            student.id
            for student in students
        ]

    # ---------------------------------------------
    # STUDENT COUNT
    # ---------------------------------------------

        student_count = len(students)

    # ---------------------------------------------
    # ACADEMIC AVERAGE
    # ---------------------------------------------

        class_average = 0

        if student_ids:

            average = (
                db.session.query(
                    func.avg(
                        AcademicRecord.total_score
                    )
                )
                .filter(
                    AcademicRecord.school_id == school_id,
                    AcademicRecord.classroom_id == classroom.id
                )
                .scalar()
            )

            class_average = round(
                average or 0,
                1
            )

    # ---------------------------------------------
    # ATTENDANCE
    # ---------------------------------------------

        class_attendance = [
            record
            for record in today_attendance
            if record.classroom_id == classroom.id
        ]

        class_present = sum(
            1
            for record in class_attendance
            if record.status == "Present"
        )

        class_attendance_percentage = 0

        if class_attendance:

            class_attendance_percentage = round(
                (
                    class_present /
                    len(class_attendance)
                ) * 100,
                1
            )

        top_classes.append({
            "classroom": classroom,
            "student_count": student_count,
            "average_score": class_average,
            "attendance": class_attendance_percentage
        })

    # Highest academic average first

    top_classes.sort(
        key=lambda item: item["average_score"],
        reverse=True
    )

    # Only show the top 5

    top_classes = top_classes[:5]
    
    
    # =====================================================
    # ATTENDANCE CHART
    # =====================================================

    attendance_chart_labels = []
    attendance_chart_data = []

    today = date.today()

    for i in range(4, -1, -1):

        current_date = today - timedelta(days=i)

        records = (
            Attendance.query
            .filter(
                Attendance.school_id == school_id,
                Attendance.attendance_date == current_date
            )
            .all()
        )

        total = len(records)

        present = sum(
            1
            for record in records
            if record.status == "Present"
        )

        if total:
            percentage = round(
                (present / total) * 100,
                1
            )
        else:
            percentage = 0

        attendance_chart_labels.append(
            current_date.strftime("%a")
        )

        attendance_chart_data.append(
            percentage
        )

    # =====================================================
    # DASHBOARD
    # =====================================================

    return render_template(
        "dashboard/dashboard.html",

        school=school,

        total_students=total_students,
        total_teachers=total_teachers,
        total_classrooms=total_classrooms,

        attendance_percentage=attendance_percentage,

        total_behaviours=total_behaviours,
        positive_behaviours=positive_behaviours,
        negative_behaviours=negative_behaviours,
        behaviour_cases=behaviour_cases,
        
        classrooms=classrooms,

        academic_average_score=academic_average_score,

        top_classes=top_classes,
        total_today_attendance=total_today_attendance,
        attendance_chart_labels=attendance_chart_labels,
        attendance_chart_data=attendance_chart_data,
        excellent_behaviours=excellent_behaviours,
        good_behaviours=good_behaviours,
        needs_attention_behaviours=needs_attention_behaviours,
        recent_activities=recent_activities
    )

@dashboard_bp.route("/dasboard_base", endpoint="dashboard_base")
def dasboard_base():
    return render_template("dashboard/dasboard_base.html")

@dashboard_bp.route("/dashboard_sidebar", endpoint="sidebar")
def sidebar():
    return render_template("dashboard/sidebar.html")

@dashboard_bp.route("/dashboard_footer", endpoint="footer")
def footer():
    return render_template("dashboard/footer.html")

@dashboard_bp.route("/dashboard_navbar", endpoint="navbar")
def navbar():
    return render_template("dashboard/navbar.html")

@dashboard_bp.route("/analytics", endpoint="analytics")
def analytics():

    return render_template(

        "dashboard/analytics.html",

        page_title="Analytics",

        page_description="Analyse trends and gain actionable insights from your school data.",

        page_icon="bi bi-bar-chart-line-fill",

        breadcrumbs=[
            {"title":"Dashboard","url":url_for("dashboard.dashboard")},
            {"title":"Analytics"}
        ],

        primary_button={
            "text":"Export Analytics",
            "icon":"bi bi-download",
            "url":"#"
        }

    )


@dashboard_bp.route("/reports", endpoint="reports")
def reports():

    return render_template(

        "dashboard/reports.html",

        page_title="Reports",

        page_description="Generate and manage school reports.",

        page_icon="bi bi-file-earmark-bar-graph-fill",

        breadcrumbs=[
            {"title":"Dashboard","url":url_for("dashboard.dashboard")},
            {"title":"Reports"}
        ],

        primary_button={
            "text":"Generate Report",
            "icon":"bi bi-plus-circle",
            "url":"url_for(dashboard.reports)"
        }

    )



@dashboard_bp.route("/profile", endpoint="profile")
def profile():

    return render_template(

        "dashboard/profile.html",

        page_title="My Profile",

        page_description="View and manage your administrator account.",

        page_icon="bi bi-person-circle",

        breadcrumbs=[
            {"title":"Dashboard","url":url_for("dashboard.dashboard")},
            {"title":"My Profile"}
        ],

        primary_button={
            "text":"Settings",
            "icon":"bi bi-gear-fill",
            "url":url_for("dashboard.settings")
        },

        user=None

    )
    
@dashboard_bp.route("/settings", endpoint="settings")
def settings():

    return render_template(

        "dashboard/settings.html",

        page_title="Settings",

        page_description="Configure your school and account preferences.",

        page_icon="bi bi-gear-fill",

        breadcrumbs=[
            {"title":"Dashboard","url":url_for("dashboard.dashboard")},
            {"title":"Settings"}
        ]

    )
    