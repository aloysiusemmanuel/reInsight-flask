"""
=========================================================
Student Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class Student(BaseModel, db.Model):
    """
    Represents a student enrolled in a school.
    """

    __tablename__ = "students"

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
        back_populates="students"
    )

    # =====================================================
    # PARENT RELATIONSHIP
    # =====================================================

    parent_id = db.Column(
        db.Integer,
        db.ForeignKey("parents.id"),
        nullable=False,
        index=True
    )

    parent = db.relationship(
        "Parent",
        back_populates="students"
    )

    # =====================================================
    # STUDENT INFORMATION
    # =====================================================

    admission_number = db.Column(
        db.String(30),
        unique=True,
        nullable=False,
        index=True
    )

    first_name = db.Column(
        db.String(100),
        nullable=False
    )

    last_name = db.Column(
        db.String(100),
        nullable=False
    )

    other_name = db.Column(
        db.String(100),
        nullable=True
    )

    gender = db.Column(
        db.String(20),
        nullable=False
    )

    date_of_birth = db.Column(
        db.Date,
        nullable=False
    )

    admission_date = db.Column(
        db.Date,
        nullable=False
    )

    photo = db.Column(
        db.String(255),
        nullable=True
    )

    # =====================================================
    # ACADEMIC INFORMATION
    # =====================================================

    classroom_id = db.Column(
    db.Integer,
    db.ForeignKey("classrooms.id"),
    nullable=False,
    index=True
    )

    classroom = db.relationship(
    "Classroom",
    back_populates="students"
    )

    stream = db.Column(
        db.String(50),
        nullable=True
    )

    academic_session = db.Column(
        db.String(20),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="Active",
        nullable=False
    )

    # =====================================================
    # MEDICAL INFORMATION
    # =====================================================

    blood_group = db.Column(
        db.String(5),
        nullable=True
    )

    genotype = db.Column(
        db.String(5),
        nullable=True
    )

    allergies = db.Column(
        db.Text,
        nullable=True
    )

    medical_conditions = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # CONTACT INFORMATION
    # =====================================================

    address = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # HELPER PROPERTIES
    # =====================================================

    @property
    def full_name(self):
        names = [
            self.first_name,
            self.other_name,
            self.last_name
        ]

        return " ".join(filter(None, names))

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return (
            f"<Student {self.admission_number} "
            f"- {self.full_name}>"
        )
    
    # =====================================================
    # RELATIONSHIPS
    # =====================================================
    academic_records = db.relationship(
        "AcademicRecord",
        back_populates="student",
        lazy=True,
        cascade="all, delete-orphan"
    )
    behaviours = db.relationship(
        "Behaviour",
        back_populates="student",
        lazy=True,
        cascade="all, delete-orphan"
    )
    attendance_records = db.relationship(
        "Attendance",
        back_populates="student",
        lazy=True,
        cascade="all, delete-orphan"
    )
    
    reports = db.relationship(
        "Report",
        back_populates="student",
        lazy=True,
        cascade="all, delete-orphan"
    )