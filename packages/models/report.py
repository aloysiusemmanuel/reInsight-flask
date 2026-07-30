"""
=========================================================
Report Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class Report(BaseModel, db.Model):
    """
    Represents a student's report card for
    a specific term and academic session.
    """

    __tablename__ = "reports"

    # =====================================================
    # RELATIONSHIPS
    # =====================================================

    school_id = db.Column(
        db.Integer,
        db.ForeignKey("schools.id"),
        nullable=False,
        index=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    classroom_id = db.Column(
        db.Integer,
        db.ForeignKey("classrooms.id"),
        nullable=False,
        index=True
    )

    teacher_id = db.Column(
        db.Integer,
        db.ForeignKey("teachers.id"),
        nullable=False,
        index=True
    )

    school = db.relationship(
        "School",
        back_populates="reports"
    )

    student = db.relationship(
        "Student",
        back_populates="reports"
    )

    classroom = db.relationship(
        "Classroom",
        back_populates="reports"
    )

    teacher = db.relationship(
        "Teacher",
        back_populates="reports"
    )

    # =====================================================
    # REPORT INFORMATION
    # =====================================================

    academic_session = db.Column(
        db.String(20),
        nullable=False
    )

    term = db.Column(
        db.String(20),
        nullable=False
    )

    # =====================================================
    # SUMMARY
    # =====================================================

    total_subjects = db.Column(
        db.Integer,
        default=0
    )

    total_score = db.Column(
        db.Float,
        default=0
    )

    average_score = db.Column(
        db.Float,
        default=0
    )

    overall_grade = db.Column(
        db.String(5),
        nullable=True
    )

    overall_position = db.Column(
        db.Integer,
        nullable=True
    )

    class_size = db.Column(
        db.Integer,
        nullable=True
    )

    # =====================================================
    # ATTENDANCE
    # =====================================================

    days_open = db.Column(
        db.Integer,
        default=0
    )

    days_present = db.Column(
        db.Integer,
        default=0
    )

    days_absent = db.Column(
        db.Integer,
        default=0
    )

    attendance_percentage = db.Column(
        db.Float,
        default=0
    )

    # =====================================================
    # COMMENTS
    # =====================================================

    class_teacher_comment = db.Column(
        db.Text,
        nullable=True
    )

    principal_comment = db.Column(
        db.Text,
        nullable=True
    )

    parent_comment = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # NEXT TERM
    # =====================================================

    next_term_begins = db.Column(
        db.Date,
        nullable=True
    )

    # =====================================================
    # STATUS
    # =====================================================

    published = db.Column(
        db.Boolean,
        default=False
    )

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return (
            f"<Report "
            f"{self.student.full_name} "
            f"{self.term} "
            f"{self.academic_session}>"
        )