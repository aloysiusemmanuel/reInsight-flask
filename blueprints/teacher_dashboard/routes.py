from flask import render_template

from . import teacher_dash_bp


# ==========================================================
# TEACHER DASHBOARD
# ==========================================================

@teacher_dash_bp.route("/")
def teacher_dashboard():
    return render_template("teacher_dash/teacher_dashboard.html")


# ==========================================================
# ATTENDANCE
# ==========================================================

@teacher_dash_bp.route("/attendance")
def attendance():
    return render_template("attendance/home.html")


@teacher_dash_bp.route("/attendance/take")
def attendance_take():
    return render_template("attendance/take.html")


@teacher_dash_bp.route("/attendance/report")
def attendance_report():
    return render_template("attendance/report.html")


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