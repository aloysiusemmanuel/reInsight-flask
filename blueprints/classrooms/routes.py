from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user
from packages.extensions import db
from packages.models.classroom import Classroom
from packages.models.teacher import Teacher
from packages.models.academic_session import AcademicSession
from packages.models import School




from . import classrooms_bp


# ==========================================================
# CLASSROOMS HOME
# ==========================================================

@classrooms_bp.route("/", endpoint="classroom")
@login_required
def classroom():

    classrooms = (
        Classroom.query
        .filter_by(is_active=True)
        .order_by(Classroom.id.asc())
        .all()
    )

    total_classrooms = len(classrooms)

    active_classrooms = total_classrooms

    assigned_teachers = sum(
        1 for c in classrooms if c.class_teacher
    )

    total_students = sum(
        len(c.students) for c in classrooms
    )

    return render_template(
        "classrooms/classroom_home.html",

        classrooms=classrooms,

        total_classrooms=total_classrooms,

        active_classrooms=active_classrooms,

        assigned_teachers=assigned_teachers,

        total_students=total_students
    )


# ==========================================================
# CREATE CLASSROOM
# ==========================================================

@classrooms_bp.route(
    "/create",
    endpoint="classroom_create",
    methods=["GET", "POST"]
)
@login_required
def classroom_create():
    
    

    
    academic_sessions = (
        AcademicSession.query
        .filter_by(
            school_id=current_user.school_id,
            is_active=True
        )
        .all()
    )

    teachers = (
        Teacher.query
        .filter_by(
            school_id=current_user.school_id,
            is_active=True
        )
        .all()
    )

    if request.method == "POST":

        try:
            
            level = request.form.get("level")
            class_name = request.form.get("class_name")
            stream = request.form.get("stream")
            capacity = request.form.get("capacity")
            academic_session_id = request.form.get("academic_session")
            teacher_id = request.form.get("teacher_id")
            description = request.form.get("description")
            
            if not level:
                raise ValueError("Please select an educational level.")

            if not class_name:
                raise ValueError("Please select a class.")

            if not academic_session_id:
                raise ValueError("Please select an academic session.")
            
            academic_session = (
                AcademicSession.query
                .filter_by(
                    id=academic_session_id,
                    school_id=current_user.school_id
                )
                .first()
            )

            if not academic_session:
                raise ValueError(
                    "Invalid academic session selected."
                )
            classroom_name = class_name

            if stream:
                classroom_name = f"{class_name} {stream}"


            classroom = Classroom(
                
                school_id=current_user.school_id,
                
                name=classroom_name,
                
                section=stream,
                
                capacity=int(capacity) if capacity else 40,

                academic_session=academic_session.session_name,

                class_teacher_id=(
                    int(teacher_id)
                    if teacher_id
                    else None
                ),
                
                description=description
            )

            db.session.add(classroom)

            db.session.commit()

            flash(
                "Classroom created successfully.",
                "success"
            )

            return redirect(
                url_for("classrooms.classroom")
            )

        except Exception as e:

            db.session.rollback()

            flash(
                f"Error creating classroom: {str(e)}",
                "danger"
            )

    return render_template(
        "classrooms/classroom_create.html",
        teachers=teachers,
        academic_sessions=academic_sessions
    )

# ==========================================================
# DEACTIVATE CLASSROOM
# ==========================================================

@classrooms_bp.route(
    "/<int:classroom_id>/deactivate",
    endpoint="classroom_deactivate",
    methods=["POST"]
)
@login_required
def classroom_deactivate(classroom_id):

    classroom = Classroom.query.get_or_404(classroom_id)

    try:

        classroom.is_active = False

        db.session.commit()

        flash(
            "Classroom deactivated successfully.",
            "warning"
        )

    except Exception as e:

        db.session.rollback()

        flash(
            f"Error deactivating classroom: {str(e)}",
            "danger"
        )

    return redirect(url_for("classrooms.classroom"))

@classrooms_bp.route("/edit<int:classroom_id>", endpoint="classroom_edit")
@login_required
def classroom_edit(classroom_id):
    
    classroom = Classroom.query.get_or_404(classroom_id)
    return render_template("classrooms/classroom_edit.html",
                           classroom=classroom)

@classrooms_bp.route("/<int:classroom_id>/profile", endpoint="classroom_profile")
@login_required
def classroom_profile(classroom_id):
    
    classroom = Classroom.query.get_or_404(classroom_id)
    return render_template("classrooms/classroom_profile.html",
                        classroom=classroom)

@classrooms_bp.route("/subjects", endpoint="classroom_subjects")
def classroom_subjects():
    return render_template("classrooms/classroom_subjects.html")

@classrooms_bp.route("/timetable", endpoint="timetable")
def timetable():
    return render_template("classrooms/timetable.html")
