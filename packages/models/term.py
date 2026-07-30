"""
=========================================================
Term Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class Term(BaseModel, db.Model):
    """
    Represents an academic term or semester within
    an academic session.

    Examples:
        First Term
        Second Term
        Third Term

        Semester 1
        Semester 2
    """

    __tablename__ = "terms"

    # =====================================================
    # ACADEMIC SESSION
    # =====================================================

    academic_session_id = db.Column(
        db.Integer,
        db.ForeignKey("academic_sessions.id"),
        nullable=False,
        index=True
    )

    academic_session = db.relationship(
        "AcademicSession",
        back_populates="terms"
    )

    # =====================================================
    # TERM INFORMATION
    # =====================================================

    term_name = db.Column(
        db.String(30),
        nullable=False
    )

    start_date = db.Column(
        db.Date,
        nullable=False
    )

    end_date = db.Column(
        db.Date,
        nullable=False
    )

    is_current = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    is_active = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )
    order = db.Column(
    db.Integer,
    nullable=False
    )

    # =====================================================
    # RELATIONSHIPS
    # =====================================================

    class_subject_assignments = db.relationship(
        "ClassSubjectAssignment",
        back_populates="term",
        lazy=True
    )

    # =====================================================
    # CONSTRAINTS
    # =====================================================

    __table_args__ = (
        db.UniqueConstraint(
            "academic_session_id",
            "term_name",
            name="uq_session_term"
        ),
    )

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return (
            f"<{self.term_name} "
            f"({self.academic_session.session_name})>"
        )