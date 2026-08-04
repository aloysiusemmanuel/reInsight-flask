from flask import render_template, url_for, request

from packages.models import Student, Classroom, Subject, AcademicSession, AcademicRecord, Term

from . import academics_bp

# ==========================================================
# ACADEMICS
# ==========================================================

@academics_bp.route("/", endpoint="academics")
def academics():
    return render_template("academics/academics_home.html")


@academics_bp.route("/results", endpoint="results")
def results():

    students = Student.query.all()
    classrooms = Classroom.query.order_by(
        Classroom.name
    ).all()

    subjects = Subject.query.order_by(
        Subject.name
    ).all()

    terms = Term.query.order_by(
        Term.id
    ).all()

    sessions = AcademicSession.query.order_by(
        AcademicSession.id.desc()
    ).all()

    return render_template(

        "academics/academics_results.html",

        students=students,

        classrooms=classrooms,

        subjects=subjects,

        terms=terms,

        sessions=sessions
    )

@academics_bp.route("/assessments", endpoint="assessments")
def assessments_home():
    students = Student.query.order_by(Student.last_name).all()
    return render_template("academics/academics_assessments.html", students=students)


@academics_bp.route("/report_cards", endpoint="report_cards")
def report_cards():
    return render_template("academics/report_cards.html")

@academics_bp.route("/class-analysis", endpoint="class_analysis")
def class_analysis():
    return render_template(
        "academics/class_analysis.html",
#         sessions=sessions,
#         terms=terms,
#         selected_session=selected_session,
#         selected_term=selected_term,
#         total_classes=total_classes,
#         total_students=total_students,
#         school_average=school_average,
#         best_class=best_class,
#         class_analysis=class_analysis
# 
    )

@academics_bp.route("/subject-analysis", endpoint="subject-analysis")
def subject_analysis():

    session_id = request.args.get("session", type=int)
    term_id = request.args.get("term", type=int)
    classroom_id = request.args.get("classroom", type=int)
    subject_id = request.args.get("subject", type=int)

    sessions = AcademicSession.query.all()
    terms = Term.query.all()
    classrooms = Classroom.query.all()
    subjects = Subject.query.all()

    records = []

    average_score = 0
    highest_score = 0
    lowest_score = 0

    if subject_id and classroom_id:

        records = (
            AcademicRecord.query
            .join(Student)
            .filter(
                AcademicRecord.subject_id == subject_id,
                Student.classroom_id == classroom_id
            )
            .all()
        )

        if records:

            totals = [record.total for record in records]

            average_score = round(
                sum(totals) / len(totals), 2
            )

            highest_score = max(totals)

            lowest_score = min(totals)

    students = Student.query.filter_by(
        classroom_id=classroom_id
    ).all() if classroom_id else []

    return render_template(

        "academics/subject_analysis.html",

        sessions=sessions,
        terms=terms,
        classrooms=classrooms,
        subjects=subjects,

        students=students,

        records=records,

        average_score=average_score,
        highest_score=highest_score,
        lowest_score=lowest_score

    )

@academics_bp.route("/analytics", endpoint="analytics")
def academics_analytics():

    return render_template(
        "academics/academics_analytics.html",

        # sessions=sessions,
        # terms=terms,

        # selected_session=selected_session,
        # selected_term=selected_term,

        # school_average=school_average,
        # highest_score=highest_score,
        # lowest_score=lowest_score,
        # pass_rate=pass_rate,

        # subject_analysis=subject_analysis,
        # class_analysis=class_analysis
    )
