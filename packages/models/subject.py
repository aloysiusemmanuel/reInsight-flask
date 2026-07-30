"""
=========================================================
Subject Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class Subject(BaseModel, db.Model):
    """
    Represents an academic subject offered by a school.
    """

    __tablename__ = "subjects"

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
        back_populates="subjects"
    )
    academic_records = db.relationship(
    "AcademicRecord",
    back_populates="subject",
    lazy=True,
    cascade="all, delete-orphan"    
    )
    
    class_assignments = db.relationship(
    "ClassSubjectAssignment",
    back_populates="subject",
    cascade="all, delete-orphan"
    )

    # =====================================================
    # SUBJECT INFORMATION
    # =====================================================

    code = db.Column(
        db.String(20),
        unique=True,
        nullable=False,
        index=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    short_name = db.Column(
        db.String(20),
        nullable=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    category = db.Column(
        db.String(50),
        nullable=True
    )

    is_core = db.Column(
        db.Boolean,
        default=True
    )

    pass_mark = db.Column(
        db.Float,
        default=40.0
    )

    maximum_score = db.Column(
        db.Float,
        default=100.0
    )

    # =====================================================
    # CLASSROOM RELATIONSHIP
    # =====================================================

    classroom_id = db.Column(
        db.Integer,
        db.ForeignKey("classrooms.id"),
        nullable=True
    )

    classroom = db.relationship(
        "Classroom",
        back_populates="subjects"
    )

    # =====================================================
    # TEACHER RELATIONSHIP
    # =====================================================

    teacher_id = db.Column(
        db.Integer,
        db.ForeignKey("teachers.id"),
        nullable=True
    )

    teacher = db.relationship(
        "Teacher",
        back_populates="subjects"
    )

    # =====================================================
    # STATUS
    # =====================================================

    status = db.Column(
        db.String(20),
        default="Active"
    )

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return f"<Subject {self.code} - {self.name}>"