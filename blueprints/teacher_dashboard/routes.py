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
# ACADEMICS HOME
# ==========================================================

@teacher_dash_bp.route("/academics", endpoint="academics_home")
def academics_home():

    stats = {
        "ca_entries": 24,
        "exam_entries": 12,
        "published_results": 8,
        "class_average": 74
    }

    activities = [
        {
            "title": "Algebra Test 1",
            "type": "CA Entry",
            "class_name": "JSS 2A",
            "date": "04 Aug 2026",
            "status": "Published"
        },
        {
            "title": "Mid-Term Examination",
            "type": "Exam Entry",
            "class_name": "JSS 2B",
            "date": "03 Aug 2026",
            "status": "Saved"
        },
        {
            "title": "Practical Worksheet",
            "type": "CA Entry",
            "class_name": "JSS 3A",
            "date": "02 Aug 2026",
            "status": "Published"
        },
        {
            "title": "Term Results",
            "type": "Result Publication",
            "class_name": "JSS 2A",
            "date": "01 Aug 2026",
            "status": "Published"
        }
    ]

    return render_template(
        "teacher_dash/academics/home.html",
        stats=stats,
        activities=activities
    )


# ==========================================================
# ACADEMICS CA
# ==========================================================

@teacher_dash_bp.route("/academics/ca", endpoint="academics_ca")
def academics_ca():

    students = [
        {"name": "David James", "admission_no": "J2A/001", "score": 18},
        {"name": "Sarah James", "admission_no": "J2A/002", "score": 16},
        {"name": "Daniel Okafor", "admission_no": "J2A/003", "score": 14},
        {"name": "Grace Bello", "admission_no": "J2A/004", "score": 19},
        {"name": "Samuel Adeyemi", "admission_no": "J2A/005", "score": 12},
    ]

    return render_template(
        "teacher_dash/academics/ca.html",
        students=students
    )


@teacher_dash_bp.route("/academics/edit")
def assessments_edit():
    return render_template("academics/edit.html")


# ==========================================================
# ACADEMICS RESULTS
# ==========================================================

@teacher_dash_bp.route("/academics/ca", endpoint="academics_results")
def academics_results():

    assessment_options = [
        {"label": "Algebra Test 1 · JSS 2A", "selected": True},
        {"label": "Comprehension Quiz · JSS 2B", "selected": False},
        {"label": "Practical Worksheet · JSS 3A", "selected": False},
    ]

    current_assessment = {
        "title": "Algebra Test 1",
        "subject": "Mathematics",
        "class_name": "JSS 2A",
        "date": "03 Aug 2026",
        "max_score": 100
    }

    summary = {
        "average": 78,
        "highest": 96,
        "lowest": 42,
        "pass_rate": 91
    }

    results = [
        {"name": "David James", "admission_no": "J2A/001", "score": 92, "grade": "A", "passed": True},
        {"name": "Sarah James", "admission_no": "J2A/002", "score": 84, "grade": "B", "passed": True},
        {"name": "Daniel Okafor", "admission_no": "J2A/003", "score": 76, "grade": "C", "passed": True},
        {"name": "Grace Bello", "admission_no": "J2A/004", "score": 68, "grade": "C", "passed": True},
        {"name": "Samuel Adeyemi", "admission_no": "J2A/005", "score": 42, "grade": "F", "passed": False},
    ]

    return render_template(
        "teacher_dash/academics/results.html",
        assessment_options=assessment_options,
        current_assessment=current_assessment,
        summary=summary,
        results=results
    )


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
# REPORTS HOME
# ==========================================================

@teacher_dash_bp.route("/reports", endpoint="reports_home")
def reports_home():

    reports = [
        {
            "title": "JSS 2A Assessment Summary",
            "type": "Assessment",
            "date": "04 Aug 2026",
            "format": "PDF"
        },
        {
            "title": "JSS 2B Attendance Report",
            "type": "Attendance",
            "date": "03 Aug 2026",
            "format": "Excel"
        },
        {
            "title": "JSS 3A Behaviour Report",
            "type": "Behaviour",
            "date": "02 Aug 2026",
            "format": "PDF"
        }
    ]

    return render_template(
        "teacher_dash/reports/home.html",
        reports=reports
    )


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
    
# ==========================================================
# EXAM ENTRY
# ==========================================================

@teacher_dash_bp.route("/academics/exam", endpoint="academics_exam")
def academics_exam():

    students = [
        {"name": "David James", "admission_no": "J2A/001", "score": 72, "grade": "A"},
        {"name": "Sarah James", "admission_no": "J2A/002", "score": 64, "grade": "B"},
        {"name": "Daniel Okafor", "admission_no": "J2A/003", "score": 58, "grade": "C"},
        {"name": "Grace Bello", "admission_no": "J2A/004", "score": 76, "grade": "A"},
        {"name": "Samuel Adeyemi", "admission_no": "J2A/005", "score": 41, "grade": "F"},
    ]

    summary = {
        "average": 62,
        "highest": 76,
        "lowest": 41,
        "pass_rate": 80
    }

    return render_template(
        "teacher_dash/academics/exam.html",
        students=students,
        summary=summary
    )