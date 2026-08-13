from flask import render_template, redirect, session, request, flash, url_for
from flask_login import login_required

from datetime import datetime

from packages.extensions import db
from packages.models import Teacher
from packages.models import User
from packages.models import Role
from packages.models import School

from . import teachers_bp


# ==========================================================
# TEACHERS
# ==========================================================

@teachers_bp.route("/", endpoint="teachers_home")
def teachers_home():
    
    columns = [
        "Staff ID",
        "Teacher Name",
        "Email",
        "Phone",
        "Status",
        "Actions"
        ]
    teachers = (
    Teacher.query
    .filter_by(is_active=True)
    .order_by(Teacher.id.asc())
    .all()
    )
 
    total_teachers = len(teachers)

    active_teachers = sum(1 for t in teachers if t.status)

    class_teachers = sum(1 for t in teachers if t.is_class_teacher)

    subject_assigned = sum(len(t.subjects) for t in teachers)
    
    return render_template("teachers/teachers_home.html",
                           teachers=teachers,
                           total_teachers=total_teachers,
                           active_teachers=active_teachers,
                           class_teachers=class_teachers,
                           subject_assigned=subject_assigned,
                           columns=columns,
                           )

# ==========================================================
# CREATE TEACHER
# ==========================================================

@teachers_bp.route("/create", endpoint="teacher_create", methods=["GET", "POST"])
def teacher_create():

    school = School.query.first()

    if school is None:
        flash("No school found.", "danger")
        return redirect(url_for("teachers.teachers"))

    teacher_role = Role.query.filter_by(name="TEACHER").first()

    if teacher_role is None:
        flash("TEACHER role not found.", "danger")
        return redirect(url_for("teachers.teachers"))

    if request.method == "POST":

        try:

            user = User(
                role_id=teacher_role.id,
                username=request.form.get("username"),
                email=request.form.get("email")
            )

            user.set_password(request.form.get("password"))

            db.session.add(user)
            db.session.flush()

            teacher = Teacher(
                school_id=school.id,
                user_id=user.id,
                staff_id = "TEMP-0000",
                first_name=request.form.get("first_name"),
                last_name=request.form.get("last_name"),
                email=request.form.get("email"),
                phone=request.form.get("phone"),
                gender=request.form.get("gender"),
                status=request.form.get("status", "Active")
            )

            db.session.add(teacher)
            db.session.flush()

            school_code = school.slug[:3].upper()

            teacher.staff_id = f"{school_code}-T-{teacher.id:04d}"

            db.session.commit()

            flash("Teacher created successfully.", "success")

            return redirect(url_for("teachers.teachers_home"))

        except Exception as e:

            db.session.rollback()

            flash(f"Error creating teacher: {str(e)}", "danger")

    return render_template("teachers/teachers_create.html")


# ==========================================================
# TEACHER PROFILE
# ==========================================================

@teachers_bp.route(
    "/<int:teacher_id>/profile",
    endpoint="teacher_profile"
)
def teacher_profile(teacher_id):

    teacher = Teacher.query.get_or_404(teacher_id)

    return render_template(
        "teachers/profile.html",
        teacher=teacher
    )
    
# ==========================================================
# EDIT TEACHER
# ==========================================================
#@login_required
@teachers_bp.route(
    "/<int:teacher_id>/edit",
    endpoint="teacher_edit",
    methods=["GET", "POST"]
)
def teacher_edit(teacher_id):

    teacher = Teacher.query.get_or_404(teacher_id)

    if request.method == "POST":

        try:

            teacher.staff_id = request.form.get(
                "staff_id"
            )

            teacher.first_name = request.form.get(
                "first_name"
            )

            teacher.last_name = request.form.get(
                "last_name"
            )

            teacher.other_name = request.form.get(
                "other_name"
            )

            teacher.email = request.form.get(
                "email"
            )

            teacher.phone = request.form.get(
                "phone"
            )

            teacher.status = request.form.get(
                "status"
            )

            db.session.commit()

            flash(
                "Teacher updated successfully.",
                "success"
            )

            return redirect(
                url_for(
                    "teachers.teacher_profile",
                    teacher_id=teacher.id
                )
            )

        except Exception as e:

            db.session.rollback()

            flash(
                f"Error updating teacher: {str(e)}",
                "danger"
            )

    return render_template(
        "teachers/edit.html",
        teacher=teacher
    )


# ==========================================================
# DELETE TEACHER
# ==========================================================

@teachers_bp.route(
    "/<int:teacher_id>/delete",
    endpoint="teacher_delete",
    methods=["POST"]
)
def teacher_delete(teacher_id):

    teacher = Teacher.query.get_or_404(teacher_id)

    try:

        teacher.is_active = False
        teacher.deactivate_at = datetime.utcnow()

        db.session.commit()

        flash(
            "Teacher deleted successfully.",
            "success"
        )

    except Exception as e:

        db.session.rollback()

        flash(
            f"Error deleting teacher: {str(e)}",
            "danger"
        )

    return redirect(
        url_for("teachers.teachers_home")
    )
    

# ==========================================================
# DEACTIVATE TEACHER
# ==========================================================

@teachers_bp.route(
    "/<int:teacher_id>/deactivate",
    endpoint="teacher_deactivate",
    methods=["POST"]
)
@login_required
def teacher_deactivate(teacher_id):

    teacher = Teacher.query.get_or_404(teacher_id)

    try:

        # Deactivate teacher profile
        teacher.status = "Suspended"
        teacher.is_active = False

        # Deactivate linked login account
        if teacher.user:
            teacher.user.is_active = False

        db.session.commit()

        flash(
            f"{teacher.full_name} has been deactivated successfully.",
            "warning"
        )

    except Exception as e:

        db.session.rollback()

        flash(
            f"Error deactivating teacher: {str(e)}",
            "danger"
        )

    return redirect(url_for("teachers.teachers_home"))
