"""
=========================================================
Academic Session Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class AcademicSession(BaseModel, db.Model):
    """
    Represents an academic session for a school.

    Examples:
        2025/2026
        2026/2027
        2027/2028
    """

    __tablename__ = "academic_sessions"

    # =====================================================
    # SCHOOL RELATIONSHIP
    # =====================================================

    school_id = db.Column(
        db.Integer,
        db.ForeignKey("schools.id"),
        nullable=False,
        index=True
    )

    school = db.relationship(
        "School",
        back_populates="academic_sessions"
    )

    # =====================================================
    # SESSION INFORMATION
    # =====================================================

    session_name = db.Column(
        db.String(20),
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

    # =====================================================
    # RELATIONSHIPS
    # =====================================================

    class_subject_assignments = db.relationship(
        "ClassSubjectAssignment",
        back_populates="academic_session",
        lazy=True
    )
    
    terms = db.relationship(
        "Term",
        back_populates="academic_session",
        cascade="all, delete-orphan",
        lazy=True
    )

    # =====================================================
    # CONSTRAINTS
    # =====================================================

    __table_args__ = (
        db.UniqueConstraint(
            "school_id",
            "session_name",
            name="uq_school_session"
        ),
    )

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return f"<AcademicSession {self.session_name}>"