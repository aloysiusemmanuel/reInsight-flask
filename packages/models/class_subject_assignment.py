from packages.extensions import db
from .base import BaseModel


class ClassSubjectAssignment(BaseModel, db.Model):
    """
    Subjects and teachers are assigned to a classroom
    for a particular academic session and term.
    """

    __tablename__ = "class_subject_assignments"

    classroom_id = db.Column(
        db.Integer,
        db.ForeignKey("classrooms.id"),
        nullable=False
    )

    subject_id = db.Column(
        db.Integer,
        db.ForeignKey("subjects.id"),
        nullable=False
    )

    teacher_id = db.Column(
        db.Integer,
        db.ForeignKey("teachers.id"),
        nullable=False
    )
    

    academic_session_id = db.Column(
        db.Integer,
        db.ForeignKey("academic_sessions.id"),
        nullable=False
    )

    term_id = db.Column(
    db.Integer,
    db.ForeignKey("terms.id"),
    nullable=False
    )

    # Relationships
    
    classroom = db.relationship(
        "Classroom",
        back_populates="subject_assignments"
    )
    term = db.relationship(
    "Term",
    back_populates="class_subject_assignments"
    )

    subject = db.relationship(
        "Subject",
        back_populates="class_assignments"
    )

    teacher = db.relationship(
        "Teacher",
        back_populates="subject_assignments"
    )
    academic_session = db.relationship(
    "AcademicSession",
    back_populates="class_subject_assignments"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "classroom_id",
            "subject_id",
            "academic_session_id",
            "term_id",
            name="uq_class_subject_session_term"
        ),
    )

    def __repr__(self):
        return (
            f"<{self.classroom.name} - "
            f"{self.subject.name} - "
            f"{self.teacher.full_name}>"
        )