from flask import render_template, request, flash, redirect, url_for, jsonify
from datetime import date

from . import teacher_dash_bp


# ==========================================================
# TEACHER DASHBOARD
# ==========================================================

@teacher_dash_bp.route("/", endpoint="teacher-dashboard")
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

@teacher_dash_bp.route("/attendance/take", methods=["GET", "POST"], endpoint="attendance-take")
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
                       endpoint="attendance-edit")
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
        return redirect(url_for("teacher_dashboard.attendance-history"))

    return render_template(
        "teacher_dash/attendance/edit.html",
        attendance=attendance,
        students=students
    )


# ==========================================================
# ACADEMICS HOME
# ==========================================================

@teacher_dash_bp.route("/academics", endpoint="academics-home")
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


from flask import render_template, request, redirect, url_for, flash

# ==========================================================
# CONTINUOUS ASSESSMENT
# ==========================================================

@teacher_dash_bp.route("/academics/ca",
                       methods=["GET", "POST"],
                       endpoint="academics-ca")
def academics_ca():

    classes = [
        {"name": "JSS 2A", "selected": True},
        {"name": "JSS 2B", "selected": False},
        {"name": "JSS 3A", "selected": False},
    ]

    subjects = [
        {"name": "Mathematics", "selected": True},
        {"name": "English", "selected": False},
        {"name": "Basic Science", "selected": False},
        {"name": "ICT", "selected": False},
    ]

    terms = [
        {"name": "First Term", "selected": True},
        {"name": "Second Term", "selected": False},
        {"name": "Third Term", "selected": False},
    ]

    assessment_types = [
        {"name": "Test 1", "selected": True},
        {"name": "Test 2", "selected": False},
        {"name": "Assignment", "selected": False},
        {"name": "Project", "selected": False},
        {"name": "Practical", "selected": False},
    ]

    students = [
        {"id": 1, "name": "David James", "admission_no": "J2A/001", "score": 18, "remark": ""},
        {"id": 2, "name": "Sarah James", "admission_no": "J2A/002", "score": 16, "remark": ""},
        {"id": 3, "name": "Daniel Okafor", "admission_no": "J2A/003", "score": 14, "remark": ""},
        {"id": 4, "name": "Grace Bello", "admission_no": "J2A/004", "score": 19, "remark": ""},
        {"id": 5, "name": "Samuel Adeyemi", "admission_no": "J2A/005", "score": 12, "remark": ""},
    ]

    if request.method == "POST":
        flash("Continuous assessment scores submitted successfully.", "success")
        return redirect(url_for("teacher_dashboard.academics-home"))

    return render_template(
        "teacher_dash/academics/ca.html",
        classes=classes,
        subjects=subjects,
        terms=terms,
        assessment_types=assessment_types,
        students=students,
        max_score=20,
        current_class="JSS 2A",
        current_subject="Mathematics",
        current_assessment="Test 1"
    )


# ==========================================================
# EDIT ACADEMIC RECORD
# ==========================================================

@teacher_dash_bp.route("/academics/edit/<int:student_id>",
                       methods=["GET", "POST"],
                       endpoint="academics-edit")
def academics_edit(student_id):

    student = {
        "id": student_id,
        "name": "David James",
        "admission_no": "J2A/001",
        "class_name": "JSS 2A",
        "subject": "Mathematics"
    }

    record = {
        "ca1": 8,
        "ca2": 9,
        "assignment": 7,
        "practical": 8,
        "ca_total": 32,
        "exam": 42,
        "total": 74,
        "grade": "B",
        "remark": "Good performance. Needs more practice in problem solving."
    }

    if request.method == "POST":
        flash("Academic record updated successfully.", "success")
        return redirect(url_for("teacher_dashboard.result-home"))

    return render_template(
        "teacher_dash/academics/edit.html",
        student=student,
        record=record
    )

# ==========================================================
# EXAMINATIONS
# ==========================================================

@teacher_dash_bp.route("/academics/exams",
                       methods=["GET", "POST"],
                       endpoint="academics-exams")
def academics_exams():

    classes = [
        {"name": "JSS 2A", "selected": True},
        {"name": "JSS 2B", "selected": False},
        {"name": "JSS 3A", "selected": False},
    ]

    subjects = [
        {"name": "Mathematics", "selected": True},
        {"name": "English", "selected": False},
        {"name": "Basic Science", "selected": False},
        {"name": "ICT", "selected": False},
    ]

    terms = [
        {"name": "First Term", "selected": True},
        {"name": "Second Term", "selected": False},
        {"name": "Third Term", "selected": False},
    ]

    exam_types = [
        {"name": "Mid-Term Exam", "selected": False},
        {"name": "End-of-Term Exam", "selected": True},
        {"name": "Mock Examination", "selected": False},
        {"name": "Final Examination", "selected": False},
    ]

    students = [
        {"id": 1, "name": "David James", "admission_no": "J2A/001", "score": 72, "grade": "A", "remark": ""},
        {"id": 2, "name": "Sarah James", "admission_no": "J2A/002", "score": 64, "grade": "B", "remark": ""},
        {"id": 3, "name": "Daniel Okafor", "admission_no": "J2A/003", "score": 58, "grade": "C", "remark": ""},
        {"id": 4, "name": "Grace Bello", "admission_no": "J2A/004", "score": 76, "grade": "A", "remark": ""},
        {"id": 5, "name": "Samuel Adeyemi", "admission_no": "J2A/005", "score": 41, "grade": "F", "remark": ""},
    ]

    if request.method == "POST":
        flash("Examination scores submitted successfully.", "success")
        return redirect(url_for("teacher_dashboard.result-home"))

    return render_template(
        "teacher_dash/academics/exams.html",
        classes=classes,
        subjects=subjects,
        terms=terms,
        exam_types=exam_types,
        students=students,
        max_score=80,
        current_class="JSS 2A",
        current_subject="Mathematics",
        current_exam="End-of-Term Examination"
    )

# ==========================================================
# RESULTS HOME
# ==========================================================

@teacher_dash_bp.route("/results", endpoint="result-home")
def results_home():

    stats = {
        "students": 120,
        "published": 8,
        "pending": 2,
        "average": 74
    }

    activities = [
        {
            "title": "First Term Results",
            "type": "Publication",
            "class_name": "JSS 2A",
            "date": "04 Aug 2026",
            "status": "Published"
        },
        {
            "title": "Mathematics Review",
            "type": "Result Review",
            "class_name": "JSS 2B",
            "date": "03 Aug 2026",
            "status": "Pending"
        },
        {
            "title": "English Results",
            "type": "Publication",
            "class_name": "JSS 3A",
            "date": "02 Aug 2026",
            "status": "Published"
        }
    ]

    return render_template(
        "teacher_dash/results/result_home.html",
        stats=stats,
        activities=activities
    )
    
# ==========================================================
# CLASS RESULT
# ==========================================================

@teacher_dash_bp.route("/results/class", endpoint="class-result")
def class_result():

    summary = {
        "students": 5,
        "average": 74,
        "highest": 96,
        "pass_rate": 80
    }

    results = [
        {"id": 1, "name": "David James", "admission_no": "J2A/001", "ca": 32, "exam": 64, "total": 96, "grade": "A", "position": 1},
        {"id": 2, "name": "Sarah James", "admission_no": "J2A/002", "ca": 28, "exam": 52, "total": 80, "grade": "B", "position": 2},
        {"id": 3, "name": "Daniel Okafor", "admission_no": "J2A/003", "ca": 24, "exam": 48, "total": 72, "grade": "B", "position": 3},
        {"id": 4, "name": "Grace Bello", "admission_no": "J2A/004", "ca": 26, "exam": 42, "total": 68, "grade": "C", "position": 4},
        {"id": 5, "name": "Samuel Adeyemi", "admission_no": "J2A/005", "ca": 18, "exam": 28, "total": 46, "grade": "F", "position": 5},
    ]

    return render_template(
        "teacher_dash/results/class_result.html",
        summary=summary,
        results=results,
        class_name="JSS 2A",
        term="First Term"
    )

# ==========================================================
# STUDENT RESULT
# ==========================================================
@teacher_dash_bp.route("/results/student/<int:student_id>", endpoint="student-result")
def student_result(student_id):
    return render_template(
        "tecaher_dash/results/student_results.html"
    )


# ==========================================================
# BEHAVIOUR HOME
# ==========================================================

@teacher_dash_bp.route("/behaviour", endpoint="behaviour-home")
def behaviour_home():

    stats = {
        "commendations": 18,
        "warnings": 7,
        "serious": 2,
        "resolved": 20
    }

    records = [
        {
            "student": "David James",
            "note": "Helped organize the classroom",
            "type": "Commendation",
            "class_name": "JSS 2A",
            "date": "04 Aug 2026",
            "status": "Resolved"
        },
        {
            "student": "Sarah James",
            "note": "Repeated talking during lesson",
            "type": "Warning",
            "class_name": "JSS 2A",
            "date": "03 Aug 2026",
            "status": "Pending"
        },
        {
            "student": "Daniel Okafor",
            "note": "Bullying complaint reported",
            "type": "Incident",
            "class_name": "JSS 3A",
            "date": "02 Aug 2026",
            "status": "Under Review"
        }
    ]

    return render_template(
        "teacher_dash/behaviour/home.html",
        stats=stats,
        records=records
    )


# ==========================================================
# CREATE BEHAVIOUR RECORD
# ==========================================================

@teacher_dash_bp.route("/behaviour/create",
                       methods=["GET", "POST"],
                       endpoint="behaviour-create")
def behaviour_create():

    students = [
        {"id": 1, "name": "David James", "admission_no": "J2A/001"},
        {"id": 2, "name": "Sarah James", "admission_no": "J2A/002"},
        {"id": 3, "name": "Daniel Okafor", "admission_no": "J2A/003"},
    ]

    classes = [
        {"id": 1, "name": "JSS 2A"},
        {"id": 2, "name": "JSS 2B"},
        {"id": 3, "name": "JSS 3A"},
    ]

    if request.method == "POST":
        flash("Behaviour record created successfully.", "success")
        return redirect(url_for("teacher_dashboard.behaviour-home"))

    return render_template(
        "teacher_dash/behaviour/create.html",
        students=students,
        classes=classes,
        today=date.today().isoformat()
    )

# ==========================================================
# BEHAVIOUR HISTORY
# ==========================================================

@teacher_dash_bp.route("/behaviour/history", endpoint="behaviour-history")
def behaviour_history():

    records = [
        {
            "id": 1,
            "student": "David James",
            "admission_no": "J2A/001",
            "class_name": "JSS 2A",
            "title": "Excellent Leadership",
            "note": "Helped organize the classroom and supported classmates.",
            "type": "Commendation",
            "date": "04 Aug 2026",
            "status": "Resolved"
        },
        {
            "id": 2,
            "student": "Sarah James",
            "admission_no": "J2A/002",
            "class_name": "JSS 2A",
            "title": "Talking During Lesson",
            "note": "Repeated talking while instructions were being given.",
            "type": "Warning",
            "date": "03 Aug 2026",
            "status": "Pending"
        },
        {
            "id": 3,
            "student": "Daniel Okafor",
            "admission_no": "J3A/003",
            "class_name": "JSS 3A",
            "title": "Bullying Complaint",
            "note": "A bullying complaint was reported by another student.",
            "type": "Incident",
            "date": "02 Aug 2026",
            "status": "Under Review"
        },
        {
            "id": 4,
            "student": "Grace Bello",
            "admission_no": "J2B/004",
            "class_name": "JSS 2B",
            "title": "Outstanding Punctuality",
            "note": "Consistently arrived early throughout the week.",
            "type": "Commendation",
            "date": "01 Aug 2026",
            "status": "Resolved"
        }
    ]

    return render_template(
        "teacher_dash/behaviour/history.html",
        records=records
    )

# ==========================================================
# EDIT BEHAVIOUR RECORD
# ==========================================================

@teacher_dash_bp.route("/behaviour/edit/<int:record_id>",
                       methods=["GET", "POST"],
                       endpoint="behaviour-edit")
def behaviour_edit(record_id):

    record = {
        "id": record_id,
        "student": "Sarah James",
        "class_name": "JSS 2A",
        "type": "Warning",
        "title": "Talking During Lesson",
        "note": "Repeated talking while instructions were being given.",
        "date": "03 Aug 2026",
        "date_input": "2026-08-03",
        "status": "Pending",
        "parent_notified": "No",
        "teacher_note": "Monitor for improvement over the next week."
    }

    if request.method == "POST":
        flash("Behaviour record updated successfully.", "success")
        return redirect(url_for("teacher_dashboard.behaviour-history"))

    return render_template(
        "teacher_dash/behaviour/edit.html",
        record=record
    )




# ==========================================================
# TIMETABLE
# ==========================================================

@teacher_dash_bp.route("/timetable")
def timetable():
    return render_template("timetable/home.html")


# ==========================================================
# REPORTS HOME
# ==========================================================

@teacher_dash_bp.route("/reports", endpoint="reports-home")
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
# ATTENDANCE HISTORY
# ==========================================================

@teacher_dash_bp.route("/attendance/history", endpoint="attendance-history")
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

@teacher_dash_bp.route("/academics/exam", endpoint="academics-exam")
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
    
#======================================================================
# GENERATE LESSON_NOTE
#======================================================================

@teacher_dash_bp.route("/lesson-notes/generate", methods=["POST"])
def generate_lesson_note(note):
    data = request.get_json()

    prompt = f"""
    Generate a professional lesson note for a Nigerian secondary school teacher.

    Class: {data['class_name']}
    Subject: {data['subject']}
    Topic: {data['topic']}
    Week: {data['week']}
    Duration: {data['duration']}

    Include:
    - Behavioural objectives
    - Prior knowledge
    - Instructional materials
    - Step-by-step presentation
    - Evaluation
    - Assignment
    """

    # Call AI provider here

    return jsonify(note)


# ==========================================================
# LESSON NOTES HOME
# ==========================================================

@teacher_dash_bp.route("/lesson-notes", endpoint="lesson-notes")
def lesson_notes():

    stats = {
        "total_notes": 24,
        "approved": 18,
        "pending": 4,
        "ai_generated": 12
    }

    notes = [
        {
            "id": 1,
            "topic": "Gradient of a Line",
            "subject": "Mathematics",
            "class_name": "JSS 2A",
            "week": 3,
            "ai_generated": True,
            "status": "Approved",
            "date": "04 Aug 2026"
        },
        {
            "id": 2,
            "topic": "Simple Interest",
            "subject": "Mathematics",
            "class_name": "JSS 2A",
            "week": 4,
            "ai_generated": False,
            "status": "Pending",
            "date": "03 Aug 2026"
        }
    ]

    return render_template(
        "teacher_dash/lesson_notes/home.html",
        stats=stats,
        notes=notes
    )
    
# ==========================================================
# CREATE LESSON NOTE
# ==========================================================

@teacher_dash_bp.route("/lesson-notes/create",
                       methods=["GET", "POST"],
                       endpoint="lesson-notes-create")
def lesson_notes_create():

    classrooms = [
        {"id": 1, "name": "JSS 2A"},
        {"id": 2, "name": "JSS 2B"},
        {"id": 3, "name": "JSS 3A"},
    ]

    subjects = [
        "Mathematics",
        "English",
        "Basic Science",
        "ICT"
    ]

    if request.method == "POST":
        flash("Lesson note created successfully.", "success")
        return redirect(url_for("teacher_dashboard.lesson-notes"))

    return render_template(
        "teacher_dash/lesson_notes/create.html",
        classrooms=classrooms,
        subjects=subjects
    )
    
# ==========================================================
# EDIT LESSON NOTE
# ==========================================================

@teacher_dash_bp.route("/lesson-notes/edit/<int:note_id>",
                       methods=["GET", "POST"],
                       endpoint="lesson-notes-edit")
def lesson_notes_edit(note_id):

    classrooms = [
        {"id": 1, "name": "JSS 2A"},
        {"id": 2, "name": "JSS 2B"},
        {"id": 3, "name": "JSS 3A"},
    ]

    subjects = [
        "Mathematics",
        "English",
        "Basic Science",
        "ICT"
    ]

    note = {
        "id": note_id,
        "classroom_id": 1,
        "class_name": "JSS 2A",
        "subject": "Mathematics",
        "week": 3,
        "duration": "40 minutes",
        "curriculum": "NERDC",
        "topic": "Gradient of a Line",
        "objectives": "Students should be able to calculate gradient.",
        "prior_knowledge": "Students know Cartesian coordinates.",
        "instructional_materials": "Graph board, ruler, marker.",
        "presentation_steps": "Introduce gradient, explain rise and run, solve examples.",
        "evaluation": "Calculate gradient of given lines.",
        "assignment": "Solve exercise 3.",
        "ai_generated": True
    }

    if request.method == "POST":
        flash("Lesson note updated successfully.", "success")
        return redirect(url_for("teacher_dashboard.lesson-notes"))

    return render_template(
        "teacher_dash/lesson_notes/lesson_edit.html",
        note=note,
        classrooms=classrooms,
        subjects=subjects
    )
    
# ==========================================================
# VIEW LESSON NOTE
# ==========================================================

@teacher_dash_bp.route("/lesson-notes/view/<int:note_id>",
                       endpoint="lesson-notes-view")
def lesson_notes_view(note_id):

    note = {
        "id": note_id,
        "class_name": "JSS 2A",
        "subject": "Mathematics",
        "week": 3,
        "topic": "Gradient of a Line"
    }

    return render_template(
        "teacher_dash/lesson_notes/view.html",
        note=note
    )
# ==========================================================
# LESSON NOTES ARCHIVE
# ==========================================================

@teacher_dash_bp.route("/lesson-notes/archive",
                       endpoint="lesson-notes-archive")
def lesson_notes_archive():

    notes = []

    return render_template(
        "teacher_dash/lesson_notes/archive.html",
        notes=notes
    )

# ==========================================================
# TEACHER PROFILE HOME
# ==========================================================

@teacher_dash_bp.route("/profile", endpoint="teacher_profile")
def teacher_profile():

    teacher = {
        "name": "Mr. David James",
        "role": "Mathematics Teacher",
        "employee_id": "TCH-1024",
        "department": "Mathematics",
        "joined": "Jan 2024",
        "email": "david.james@school.com",
        "phone": "+234 801 234 5678",
        "gender": "Male",
        "address": "Lagos, Nigeria",
        "classes": 5,
        "students": 182,
        "notes": 24
    }

    return render_template(
        "teacher_dash/profile/home.html",
        teacher=teacher
    )
    
# ==========================================================
# TEACHER PROFILE PREFERENCES
# ==========================================================

@teacher_dash_bp.route("/profile/preferences",
                       methods=["GET", "POST"],
                       endpoint="profile-preferences")
def profile_preferences():

    preferences = {
        "theme": "light",
        "density": "comfortable",
        "show_avatars": True,
        "email_notifications": True,
        "result_notifications": True,
        "behaviour_notifications": False,
        "weekly_summary": True,
        "enable_ai": True,
        "curriculum": "NERDC",
        "ai_style": "detailed",
        "auto_objectives": True,
        "two_factor": False,
        "session_timeout": True,
        "language": "English"
    }

    if request.method == "POST":
        flash("Preferences updated successfully.", "success")
        return redirect(url_for("teacher_dashboard.profile-preferences"))

    return render_template(
        "teacher_dash/profile/preferences.html",
        preferences=preferences
    )
    
# ==========================================================
# TEACHER PROFILE EDIT
# ==========================================================

@teacher_dash_bp.route("/profile/edit",
                       methods=["GET", "POST"],
                       endpoint="profile-edit")
def profile_edit():

    teacher = {
        "name": "Mr. David James",
        "first_name": "David",
        "last_name": "James",
        "role": "Mathematics Teacher",
        "employee_id": "TCH-1024",
        "department": "Mathematics",
        "subject": "Mathematics",
        "qualification": "B.Sc. Mathematics",
        "email": "david.james@school.com",
        "phone": "+234 801 234 5678",
        "gender": "Male",
        "dob": "1990-05-15",
        "address": "Lagos, Nigeria"
    }

    if request.method == "POST":
        flash("Profile updated successfully.", "success")
        return redirect(url_for("teacher_dashboard.teacher_profile"))

    return render_template(
        "teacher_dash/profile/edit.html",
        teacher=teacher
    )


# ==========================================================
# TEACHER PROFILE SECURITY
# ==========================================================

@teacher_dash_bp.route("/profile/security", endpoint="profile-security")
def profile_security():
    return render_template("teacher_dash/profile/security.html")

# ==========================================================
# TEACHER SETTINGS HOME
# ==========================================================

@teacher_dash_bp.route("/settings", endpoint="teacher-settings")
def teacher_settings():
    return render_template("teacher_dash/settings/home.html")