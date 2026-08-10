from flask import render_template, redirect, request, flash, url_for
from datetime import datetime

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

    students = (
        Student.query
        .order_by(
            Student.first_name.asc(),
            Student.last_name.asc(),
            Student.other_name.asc()
        )
        .all()
    )

    rows = []

    for student in students:

        parent_name = "-"

        if student.parent:
            parent_name = (
                f"{student.parent.first_name} "
                f"{student.parent.last_name}"
            )

        classroom_name = "-"

        if student.classroom:
            classroom_name = student.classroom.name

        actions = (
            f'<a href="{url_for("students.student_profile", student_id=student.id)}" '
            f'class="btn btn-sm btn-outline-primary me-1">View</a>'
            f'<a href="{url_for("students.student_edit", student_id=student.id)}" '
            f'class="btn btn-sm btn-outline-secondary me-1">Edit</a>'
        )

        rows.append([
            student.admission_number,
            student.full_name,
            student.gender,
            classroom_name,
            parent_name,
            student.status,
            actions
        ])

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

        page_description=(
            "Manage student admissions, profiles, "
            "promotions and reports."
        ),

        page_icon="bi bi-mortarboard-fill",

        breadcrumbs=[
            {
                "title": "Dashboard",
                "url": url_for("dashboard.dashboard")
            },
            {
                "title": "Students"
            }
        ],

        primary_button={
            "text": "Add Student",
            "icon": "bi bi-plus-circle",
            "url": url_for("students.student_create")
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

# ==========================================================
# CREATE STUDENT
# ==========================================================

@students_bp.route(
    "/create",
    endpoint="student_create",
    methods=["GET", "POST"]
)
def student_create():

    if request.method == "POST":

        try:

            date_of_birth = datetime.strptime(
                request.form.get("date_of_birth"),
                "%Y-%m-%d"
            ).date()

            admission_date = datetime.strptime(
                request.form.get("admission_date"),
                "%Y-%m-%d"
            ).date()

            student = Student(

                school_id=1,   # TODO: i will replace with current_user.school_id when auth is complete

                parent_id=int(
                    request.form.get("parent_id")
                ),

                classroom_id=int(
                    request.form.get("classroom_id")
                ),

                admission_number=request.form.get(
                    "admission_number"
                ),

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

                date_of_birth=date_of_birth,

                admission_date=admission_date,

                academic_session=request.form.get(
                    "academic_session"
                ),

                status=request.form.get(
                    "status",
                    "Active"
                ),

                stream=request.form.get(
                    "stream"
                ),

                address=request.form.get(
                    "address"
                ),

                blood_group=request.form.get(
                    "blood_group"
                ),

                genotype=request.form.get(
                    "genotype"
                ),

                allergies=request.form.get(
                    "allergies"
                ),

                medical_conditions=request.form.get(
                    "medical_conditions"
                )

            )

            db.session.add(student)

            db.session.commit()

            flash(
                "Student created successfully.",
                "success"
            )

            return redirect(
                url_for("students.students")
            )

        except Exception as e:

            db.session.rollback()

            flash(
                f"Error creating student: {str(e)}",
                "danger"
            )

    parents = (
        Parent.query
        .order_by(Parent.first_name.asc(), Parent.last_name.asc())
        .all()
    )

    classrooms = (
        Classroom.query
        .order_by(Classroom.name.asc())
        .all()
    )

    return render_template(

        "students/create.html",

        parents=parents,

        classrooms=classrooms
    )

        

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

# ==========================================================
# EDIT STUDENT
# ==========================================================

@students_bp.route(
    "/<int:student_id>/edit",
    endpoint="student_edit",
    methods=["GET", "POST"]
)
def student_edit(student_id):

    student = Student.query.get_or_404(student_id)

    if request.method == "POST":

        try:

            student.parent_id = int(
                request.form.get("parent_id")
            )

            student.classroom_id = int(
                request.form.get("classroom_id")
            )

            student.admission_number = request.form.get(
                "admission_number"
            )

            student.first_name = request.form.get(
                "first_name"
            )

            student.last_name = request.form.get(
                "last_name"
            )

            student.other_name = request.form.get(
                "other_name"
            )

            student.gender = request.form.get(
                "gender"
            )

            student.date_of_birth = datetime.strptime(
                request.form.get("date_of_birth"),
                "%Y-%m-%d"
            ).date()

            student.admission_date = datetime.strptime(
                request.form.get("admission_date"),
                "%Y-%m-%d"
            ).date()

            student.academic_session = request.form.get(
                "academic_session"
            )

            student.status = request.form.get(
                "status"
            )

            student.stream = request.form.get(
                "stream"
            )

            student.address = request.form.get(
                "address"
            )

            student.blood_group = request.form.get(
                "blood_group"
            )

            student.genotype = request.form.get(
                "genotype"
            )

            student.allergies = request.form.get(
                "allergies"
            )

            student.medical_conditions = request.form.get(
                "medical_conditions"
            )

            db.session.commit()

            flash(
                "Student updated successfully.",
                "success"
            )

            return redirect(
                url_for(
                    "students.student_details",
                    student_id=student.id
                )
            )

        except Exception as e:

            db.session.rollback()

            flash(
                f"Error updating student: {str(e)}",
                "danger"
            )

    parents = Parent.query.all()

    classrooms = Classroom.query.all()

    return render_template(

        "students/edit.html",

        student=student,

        parents=parents,

        classrooms=classrooms
    )

# ==========================================================
# DELETE STUDENT
# ==========================================================

@students_bp.route(
    "/<int:student_id>/delete",
    endpoint="student_delete",
    methods=["POST"]
)
def student_delete(student_id):

    student = Student.query.get_or_404(student_id)

    try:

        db.session.delete(student)

        db.session.commit()

        flash(
            "Student deleted successfully.",
            "success"
        )

    except Exception as e:

        db.session.rollback()

        flash(
            f"Error deleting student: {str(e)}",
            "danger"
        )

    return redirect(
        url_for("students.students")
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
