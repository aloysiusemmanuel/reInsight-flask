from flask import render_template, redirect, request, flash, url_for

from packages.extensions import db

from packages.models import Student, Classroom, Parent

from . import students_bp

from blueprints.attendance.services import get_student_attendance

# ==========================================================
# STUDENTS
# ==========================================================


@students_bp.route("/", endpoint="students")
def students():
    columns = [
    "Admission No.",
    "Student Name",
    "Gender",
    "Class",
    "Parent",
    "Status",
    "Actions"
    ]

    rows = []
    students = Student.query.all()

    student_count = Student.query.count()

    male_count = Student.query.filter_by(
        gender="Male"
    ).count()

    female_count = Student.query.filter_by(
        gender="Female"
    ).count()

    return render_template(

        "students/student_home.html",

        page_title="Students",

        page_description="Manage student admissions, profiles, promotions and reports.",

        page_icon="bi bi-mortarboard-fill",

        breadcrumbs=[
            {"title":"Dashboard",
             "url":url_for("dashboard.dashboard")},
            {"title":"Students"}
        ],

        primary_button={
            "text":"Add Student",
            "icon":"bi bi-plus-circle",
            "url":url_for("students.student_create")
        },
        students=students,
        student_count=student_count,
        male_count=male_count,
        female_count=female_count,
        new_students=0,
        table_title="Student Directory",
        table_description="All registered students",
        columns=columns,
        rows=rows

    )

# =========================================================
# CREATE
# =========================================================
@students_bp.route("/create", endpoint="student_create", methods=["GET", "POST"])
def student_create():
    
    if request.method == "POST":

        student = Student(

            first_name=request.form.get(
                "first_name"
            ),

            last_name=request.form.get(
                "last_name"
            ),

            other_name=request.form.get(
                "other_name"
            ),

            gender=request.form.get(
                "gender"
            ),

            admission_number=request.form.get(
                "admission_number"
            )

        )


        db.session.add(student)

        db.session.commit()


        flash(
            "Student created successfully",
            "success"
        )


        return redirect(
            url_for("students.dashboard")
        )


    parents = Parent.query.all()

    classrooms = Classroom.query.all()
    return render_template("students/create.html", parents=parents, classrooms=classrooms)

# =========================================================
# PROFILE
# =========================================================

@students_bp.route("/profile/<int:student_id>", endpoint="student_profile")
def student_profile(student_id):
    
    student = Student.query.get_or_404(student_id)

    return render_template(

        "students/profile.html",

        student=student,

        page_title="Student Profile",

        page_description="View complete student information.",

        page_icon="bi bi-person-badge-fill",

        breadcrumbs=[
            {"title": "Dashboard", "url": url_for("dashboard.dashboard")},
            {"title": "Students", "url": url_for("students.students")},
            {"title": "Profile"}
        ],

        primary_button={
            "text": "Edit Student",
            "icon": "bi bi-pencil-square",
            "url": url_for("students.student_edit", student_id=student_id)
        }

    )

# =========================================================
# EDIT
# =========================================================

@students_bp.route("/edit<int:student_id>", endpoint="student_edit", methods=["GET", "POST"])
def student_edit(student_id):
    student = Student.query.get_or_404(
        student_id
    )
    
    if request.method == "POST":


        student.first_name = request.form.get(
            "first_name"
        )


        student.last_name = request.form.get(
            "last_name"
        )


        student.gender = request.form.get(
            "gender"
        )


        db.session.commit()


        flash(
            "Student updated successfully",
            "success"
        )


        return redirect(
            url_for(
                "students.student_profile",
                student_id=student.id
            )
        )


    classrooms = Classroom.query.all()

    parents = Parent.query.all()
    return render_template(
        "students/edit.html",
        student=student, classrooms=classrooms, parents=parents
    )

# =========================================================
# PROMOTION
# =========================================================

@students_bp.route("/promotion/<int:student_id>", endpoint="student_promotion", methods=["GET", "POST"])
def student_promotions(student_id):
    student = Student.query.get_or_404(
        student_id
    )
    if request.method == "POST":


        student.classroom_id = request.form.get(
            "new_classroom"
        )


        db.session.commit()


        flash(
            "Student promoted successfully",
            "success"
        )


        return redirect(
            url_for(
                "student_profile",
                student_id=student.id
            )
        )


    classrooms = Classroom.query.all()


    return render_template(
        "students/promotion.html",
        student=student,
        classrooms=classrooms
    )

# =========================================================
# REPORTS
# =========================================================

@students_bp.route("/reports/<int:student_id>", endpoint="student_report")
def student_reports(student_id):


    student = Student.query.get_or_404(
        student_id
    )


    reports = []


    return render_template(
        "students/reports.html",
        student=student,
        reports=reports
    )
    
# =========================================================
# ATTENDANCE
# =========================================================  
@students_bp.route("/attendance/<int:student_id>", endpoint="student_attendance")
def student_attendance(student_id):


    student = Student.query.get_or_404(
        student_id
    )


    records = get_student_attendance(id)


    return render_template(
        "students/attendance.html",
        student=student,
        records=records
    )



# =========================================================
# BEHAVIOUR
# =========================================================

@students_bp.route("/behaviour/<int:student_id>", endpoint="student_behaviour")
def student_behaviour(student_id):


    student = Student.query.get_or_404(
        student_id
    )


    behaviours = []


    return render_template(
        "students/behaviour.html",
        student=student,
        behaviours=behaviours
    )



# =========================================================
# ACADEMIC RECORD
# =========================================================

@students_bp.route("/academic_record/<int:student_id>", endpoint="student_academic_record")
def student_academic_record(student_id):


    student = Student.query.get_or_404(
        student_id
    )


    academic_records = []


    return render_template(
        "students/academic_record.html",
        student=student,
        academic_records=academic_records
    )
