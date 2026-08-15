from flask import render_template, url_for, request

from packages.models import Classroom, Student

from . import attendance_bp

# ==========================================================
# ATTENDANCE
# ==========================================================

@attendance_bp.route("/", endpoint="attendance_home")
def attendance_home():
    return render_template("attendance/attendance_home.html")


@attendance_bp.route("/take", endpoint="attendance_take", methods=["GET", "POST"])
def attendance_take():

    classrooms = Classroom.query.order_by(Classroom.name).all()

    classroom_id = request.args.get("classroom_id", type=int)

    students = []

    if classroom_id:
        students = Student.query.filter_by(
            classroom_id=classroom_id
        ).order_by(
            Student.last_name,
            Student.first_name
        ).all()

    return render_template(
        "attendance/attendance_take.html",
        classrooms=classrooms,
        students=students,
        selected_classroom=classroom_id
    )

@attendance_bp.route("/history/<int:student_id>", endpoint="attendance_history")
def attendance_history(student_id):
    return render_template("attendance/attendance_history.html", student=student_id )


@attendance_bp.route("/report", endpoint="attendance_report")
def attendance_report():
    return render_template("attendance/attendance_report.html")