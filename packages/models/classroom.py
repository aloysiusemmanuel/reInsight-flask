"""
=========================================================
Classroom Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class Classroom(BaseModel, db.Model):
    """
    Represents a classroom or class within a school.
    """

    __tablename__ = "classrooms"

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
        back_populates="classrooms"
    )

    # =====================================================
    # CLASS TEACHER
    # =====================================================

    class_teacher_id = db.Column(
        db.Integer,
        db.ForeignKey("teachers.id"),
        nullable=True
    )

    class_teacher = db.relationship(
        "Teacher",
        back_populates="classrooms"
    )

    # =====================================================
    # CLASS INFORMATION
    # =====================================================

    name = db.Column(
        db.String(50),
        nullable=False
    )

    section = db.Column(
        db.String(30),
        nullable=True
    )

    academic_session = db.Column(
        db.String(20),
        nullable=False
    )

    capacity = db.Column(
        db.Integer,
        default=40
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # RELATIONSHIPS
    # =====================================================
    
    subject_assignments = db.relationship(
    "ClassSubjectAssignment",
    back_populates="classroom",
    cascade="all, delete-orphan"
    )

    students = db.relationship(
        "Student",
        back_populates="classroom",
        lazy=True
    )
    
    subjects = db.relationship(
        "Subject",
        back_populates="classroom",
        lazy=True,
        cascade="all, delete-orphan"
    )
   
    academic_records = db.relationship(
        "AcademicRecord",
        back_populates="classroom",
        lazy=True,
        cascade="all, delete-orphan"
    )
    reports = db.relationship(
        "Report",
        back_populates="classroom",
        lazy=True,
        cascade="all, delete-orphan"    
    )   
    behaviours = db.relationship(
        "Behaviour",
        back_populates="classroom",
        lazy=True,
        cascade="all, delete-orphan"
    )
    attendance_records = db.relationship(
        "Attendance",
        back_populates="classroom",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return f"<Classroom {self.name}>"