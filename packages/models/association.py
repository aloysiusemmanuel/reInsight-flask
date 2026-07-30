

from packages.extensions import db

teacher_subjects = db.Table(
    "teacher_subjects",

    db.Column(
        "teacher_id",
        db.Integer,
        db.ForeignKey("teachers.id"),
        primary_key=True
    ),

    db.Column(
        "subject_id",
        db.Integer,
        db.ForeignKey("subjects.id"),
        primary_key=True
    )
)


teacher_classrooms = db.Table(
    "teacher_classrooms",

    db.Column(
        "teacher_id",
        db.Integer,
        db.ForeignKey("teachers.id"),
        primary_key=True
    ),

    db.Column(
        "classroom_id",
        db.Integer,
        db.ForeignKey("classrooms.id"),
        primary_key=True
    )
)