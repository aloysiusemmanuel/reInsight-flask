"""
=========================================================
Behaviour Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class Behaviour(BaseModel, db.Model):
    """
    Stores a student's behavioural record.
    """

    __tablename__ = "behaviours"

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

    teacher_id = db.Column(
        db.Integer,
        db.ForeignKey("teachers.id"),
        nullable=False,
        index=True
    )

    classroom_id = db.Column(
        db.Integer,
        db.ForeignKey("classrooms.id"),
        nullable=False,
        index=True
    )

    school = db.relationship(
        "School",
        back_populates="behaviours"
    )

    student = db.relationship(
        "Student",
        back_populates="behaviours"
    )

    teacher = db.relationship(
        "Teacher",
        back_populates="behaviours"
    )

    classroom = db.relationship(
        "Classroom",
        back_populates="behaviours"
    )

    # =====================================================
    # ACADEMIC PERIOD
    # =====================================================

    academic_session = db.Column(
        db.String(20),
        nullable=False
    )

    term = db.Column(
        db.String(20),
        nullable=False
    )

    behaviour_date = db.Column(
        db.Date,
        nullable=False
    )

    # =====================================================
    # BEHAVIOUR DETAILS
    # =====================================================

    category = db.Column(
        db.String(50),
        nullable=False
    )
    # Example:
    # Discipline
    # Leadership
    # Attendance
    # Participation
    # Respect
    # Honesty
    # Teamwork

    behaviour_type = db.Column(
        db.String(20),
        nullable=False
    )
    # Positive
    # Negative

    severity = db.Column(
        db.String(20),
        default="Low"
    )
    # Low
    # Medium
    # High
    # Critical

    title = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    action_taken = db.Column(
        db.Text,
        nullable=True
    )

    parent_notified = db.Column(
        db.Boolean,
        default=False
    )

    resolved = db.Column(
        db.Boolean,
        default=False
    )

    # =====================================================
    # BEHAVIOUR SCORE
    # =====================================================

    behaviour_points = db.Column(
        db.Integer,
        default=0
    )
    
    submission_status = db.Column(
    db.String(20),
    default="Draft"
    )
    # Positive values reward good behaviour.
    # Negative values can be used for misconduct.

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return (
            f"<Behaviour "
            f"{self.student.full_name} - "
            f"{self.behaviour_type}>"
        )