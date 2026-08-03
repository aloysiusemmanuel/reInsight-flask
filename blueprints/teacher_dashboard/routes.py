from flask import render_template, request, flash, redirect, url_for

from . import teacher_dash_bp


# ==========================================================
# TEACHER DASHBOARD
# ==========================================================

@teacher_dash_bp.route("/")
def teacher_dashboard():
    return render_template("teacher_dash/teacher_dashboard.html")



@teacher_dash_bp.route("/classes")
def classes_home():
    return render_template("teacher_dash/classes/home.html")

@teacher_dash_bp.route("/show")
def show():
    return render_template("teacher_dash/classes/show.html")



# ==========================================================
# ATTENDANCE HOME
# ==========================================================

@teacher_dash_bp.route("/attendance", endpoint="attendance")
def attendance():

    stats = {
        "total_students": 124,
        "present": 116,
        "late": 5,
        "absent": 3
    }

    classes = [
        {   
            "id": 1,
            "name": "JSS 2A",
            "time": "8:00 AM - 9:00 AM",
            "students": 32,
            "recorded": 32
        },
        {
            "id": 2,
            "name": "JSS 2B",
            "time": "9:15 AM - 10:15 AM",
            "students": 30,
            "recorded": 28
        },
        {
            "id": 3,
            "name": "JSS 3A",
            "time": "11:00 AM - 12:00 PM",
            "students": 31,
            "recorded": 31
        }
    ]

    records = [
        {
            "id": 2,
            "class_name": "JSS 2A",
            "date": "03 Aug 2026",
            "status": "Completed",
            "teacher": "You"
        },
        {
            "id": 2,
            "class_name": "JSS 2B",
            "date": "03 Aug 2026",
            "status": "Pending",
            "teacher": "You"
        },
        {
            "id": 3,
            "class_name": "JSS 3A",
            "date": "02 Aug 2026",
            "status": "Completed",
            "teacher": "You"
        }
    ]

    return render_template(
        "teacher_dash/attendance/home.html",
        stats=stats,
        classes=classes,
        records=records,
        today_date="Monday, 3 August 2026"
    )


# ==========================================================
# TAKE ATTENDANCE
# ==========================================================

@teacher_dash_bp.route("/attendance/take", methods=["GET", "POST"], endpoint="attendance_take")
def attendance_take():

    classes = [
        {"name": "JSS 2A", "selected": True},
        {"name": "JSS 2B", "selected": False},
        {"name": "JSS 3A", "selected": False},
    ]

    selected_class = {"name": "JSS 2A"}

    students = [
        {"id": 1, "name": "David James", "admission_no": "J2A/001", "avatar": None},
        {"id": 2, "name": "Sarah James", "admission_no": "J2A/002", "avatar": None},
        {"id": 3, "name": "Daniel Okafor", "admission_no": "J2A/003", "avatar": None},
        {"id": 4, "name": "Grace Bello", "admission_no": "J2A/004", "avatar": None},
        {"id": 5, "name": "Samuel Adeyemi", "admission_no": "J2A/005", "avatar": None},
    ]

    if request.method == "POST":
        flash("Attendance submitted successfully.", "success")
        return redirect(url_for("teacher_dashboard.attendance"))

    return render_template(
        "teacher_dash/attendance/take.html",
        classes=classes,
        selected_class=selected_class,
        students=students,
        selected_date="2026-08-03"
    )


# ==========================================================
# EDIT ATTENDANCE
# ==========================================================

@teacher_dash_bp.route("/attendance/edit/<int:record_id>",
                       methods=["GET", "POST"],
                       endpoint="attendance_edit")
def attendance_edit(record_id):

    attendance = {
        "id": record_id,
        "class_name": "JSS 2A",
        "date": "03 Aug 2026",
        "total": 32,
        "present": 31,
        "late": 1,
        "absent": 0
    }

    students = [
        {
            "id": 1,
            "name": "David James",
            "admission_no": "J2A/001",
            "status": "present",
            "remark": ""
        },
        {
            "id": 2,
            "name": "Sarah James",
            "admission_no": "J2A/002",
            "status": "late",
            "remark": "Arrived after assembly"
        },
        {
            "id": 3,
            "name": "Daniel Okafor",
            "admission_no": "J2A/003",
            "status": "present",
            "remark": ""
        },
        {
            "id": 4,
            "name": "Grace Bello",
            "admission_no": "J2A/004",
            "status": "present",
            "remark": ""
        },
        {
            "id": 5,
            "name": "Samuel Adeyemi",
            "admission_no": "J2A/005",
            "status": "absent",
            "remark": "Medical leave"
        },
    ]

    if request.method == "POST":
        flash("Attendance updated successfully.", "success")
        return redirect(url_for("teacher_dashboard.attendance_history"))

    return render_template(
        "teacher_dash/attendance/edit.html",
        attendance=attendance,
        students=students
    )


# ==========================================================
# ASSESSMENT
# ==========================================================

@teacher_dash_bp.route("/assessment")
def assessment():
    return render_template("assessment/home.html")


@teacher_dash_bp.route("/assessment/create")
def assessment_create():
    return render_template("assessment/create.html")


@teacher_dash_bp.route("/assessment/edit")
def assessment_edit():
    return render_template("assessment/edit.html")


# ==========================================================
# RESULTS
# ==========================================================

@teacher_dash_bp.route("/results")
def results():
    return render_template("results/home.html")


@teacher_dash_bp.route("/results/class")
def class_results():
    return render_template("results/class_results.html")


@teacher_dash_bp.route("/results/subject")
def subject_results():
    return render_template("results/subject_results.html")


# ==========================================================
# BEHAVIOUR
# ==========================================================

@teacher_dash_bp.route("/behaviour")
def behaviour():
    return render_template("behaviour/home.html")


@teacher_dash_bp.route("/behaviour/create")
def behaviour_create():
    return render_template("behaviour/create.html")


# ==========================================================
# LESSON NOTES
# ==========================================================

@teacher_dash_bp.route("/lesson-notes")
def lesson_notes():
    return render_template("lesson_notes/home.html")


@teacher_dash_bp.route("/lesson-notes/create")
def lesson_note_create():
    return render_template("lesson_notes/create.html")


# ==========================================================
# TIMETABLE
# ==========================================================

@teacher_dash_bp.route("/timetable")
def timetable():
    return render_template("timetable/home.html")


# ==========================================================
# REPORTS
# ==========================================================

@teacher_dash_bp.route("/reports")
def reports():
    return render_template("reports/home.html")


# ==========================================================
# PROFILE
# ==========================================================

@teacher_dash_bp.route("/profile")
def profile():
    return render_template("profile/home.html")


# ==========================================================
# SETTINGS
# ==========================================================

@teacher_dash_bp.route("/settings")
def settings():
    return render_template("settings/home.html")

# ==========================================================
# ATTENDANCE HISTORY
# ==========================================================

@teacher_dash_bp.route("/attendance/history", endpoint="attendance_history")
def attendance_history():

    summary = {
        "records": 18,
        "present": 542,
        "late": 23,
        "absent": 17
    }

    records = [
        {
            "id": 1,
            "date": "03 Aug 2026",
            "day": "Monday",
            "class_name": "JSS 2A",
            "total": 32,
            "present": 31,
            "late": 1,
            "absent": 0,
            "rate": 97,
            "status": "Completed"
        },
        {
            "id": 2,
            "date": "03 Aug 2026",
            "day": "Monday",
            "class_name": "JSS 2B",
            "total": 30,
            "present": 27,
            "late": 2,
            "absent": 1,
            "rate": 90,
            "status": "Completed"
        },
        {
            "id": 3,
            "date": "02 Aug 2026",
            "day": "Sunday",
            "class_name": "JSS 3A",
            "total": 31,
            "present": 30,
            "late": 0,
            "absent": 1,
            "rate": 97,
            "status": "Completed"
        },
        {
            "id": 4,
            "date": "01 Aug 2026",
            "day": "Saturday",
            "class_name": "JSS 2A",
            "total": 32,
            "present": 29,
            "late": 1,
            "absent": 2,
            "rate": 91,
            "status": "Completed"
        },
        {
            "id": 4,
            "date": "31 Jul 2026",
            "day": "Friday",
            "class_name": "JSS 2B",
            "total": 30,
            "present": 28,
            "late": 1,
            "absent": 1,
            "rate": 93,
            "status": "Draft"
        }
    ]

    return render_template(
        "teacher_dash/attendance/history.html",
        summary=summary,
        records=records
    )