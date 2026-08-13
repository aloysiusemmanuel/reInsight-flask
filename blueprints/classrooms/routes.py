from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from packages.extensions import db
from packages.models.classroom import Classroom
from packages.models.teacher import Teacher




from . import classrooms_bp



# ==========================================================
# CLASSROOM
# ==========================================================

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

    teachers = Teacher.query.filter_by(
        is_active=True
    ).all()

    if request.method == "POST":

        try:

            classroom = Classroom(

                name=request.form.get("name"),

                section=request.form.get("section"),

                capacity=int(request.form.get("capacity", 40)),

                academic_session=request.form.get("academic_session"),

                class_teacher_id=request.form.get("class_teacher_id") or None
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
        "classrooms/create.html",
        teachers=teachers
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

@classrooms_bp.route("/edit", endpoint="classroom_edit")
def classroom_edit():
    return render_template("classrooms/classroom_edit.html")

@classrooms_bp.route("/profile", endpoint="classroom_profile")
def classroom_profile():
    return render_template("classrooms/classroom_profile.html")

@classrooms_bp.route("/subjects", endpoint="classroom_subjects")
def classroom_subjects():
    return render_template("classrooms/classroom_subjects.html")

@classrooms_bp.route("/timetable", endpoint="timetable")
def timetable():
    return render_template("classrooms/timetable.html")
