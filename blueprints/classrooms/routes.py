from flask import render_template, redirect, session, request, flash, url_for

from . import classrooms_bp



# ==========================================================
# CLASSROOM
# ==========================================================

@classrooms_bp.route("", endpoint="classroom")
def classroom():
    return render_template("classrooms/classroom_home.html")


@classrooms_bp.route("/create", endpoint="classroom_create")
def classroom_create():
    return render_template("classrooms/classroom_create.html")

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
