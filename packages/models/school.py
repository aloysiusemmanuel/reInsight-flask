"""
=========================================================
School Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class School(BaseModel, db.Model):
    """
    Represents a school registered on the reInsight platform.
    """

    __tablename__ = "schools"

    # =====================================================
    # BASIC INFORMATION
    # =====================================================

    name = db.Column(
        db.String(200),
        nullable=False
    )

    slug = db.Column(
        db.String(200),
        unique=True,
        nullable=False,
        index=True
    )
    
    code = db.Column(
        db.String(20),
        unique=True,
        nullable=False,
        index=True
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    phone = db.Column(
        db.String(20),
        nullable=False
    )

    website = db.Column(
        db.String(255),
        nullable=True
    )

    logo = db.Column(
        db.String(255),
        nullable=True
    )

    # =====================================================
    # ADDRESS
    # =====================================================

    address = db.Column(
        db.String(255),
        nullable=False
    )

    city = db.Column(
        db.String(100),
        nullable=True
    )

    state = db.Column(
        db.String(100),
        nullable=True
    )

    country = db.Column(
        db.String(100),
        default="Nigeria",
        nullable=False
    )

    postal_code = db.Column(
        db.String(20),
        nullable=True
    )

    # =====================================================
    # SCHOOL INFORMATION
    # =====================================================
    
    classrooms = db.relationship(
    "Classroom",
    back_populates="school",
    lazy=True,
    cascade="all, delete-orphan"
    )

    school_type = db.Column(
        db.String(50),
        nullable=False,
        default="Secondary"
    )

    ownership = db.Column(
        db.String(50),
        nullable=True
    )

    motto = db.Column(
        db.String(255),
        nullable=True
    )

    established_year = db.Column(
        db.Integer,
        nullable=True
    )

    # =====================================================
    # SUBSCRIPTION
    # =====================================================

    subscription_plan = db.Column(
        db.String(50),
        default="Demo",
        nullable=False
    )

    subscription_status = db.Column(
        db.String(30),
        default="Pending",
        nullable=False
    )

    demo_expires_at = db.Column(
        db.DateTime,
        nullable=True
    )

    subscription_expires_at = db.Column(
        db.DateTime,
        nullable=True
    )

    # =====================================================
    # RELATIONSHIPS
    # =====================================================
    
    users = db.relationship(
    "User",
    back_populates="school",
    lazy=True,
    cascade="all, delete-orphan"
    )

    administrators = db.relationship(
        "SchoolAdmin",
        back_populates="school",
        lazy=True,
        cascade="all, delete-orphan"
    )

    teachers = db.relationship(
        "Teacher",
        back_populates="school",
        lazy=True,
        cascade="all, delete-orphan"
    )

    parents = db.relationship(
        "Parent",
        back_populates="school",
        lazy=True,
        cascade="all, delete-orphan"
    )

    students = db.relationship(
        "Student",
        back_populates="school",
        lazy=True,
        cascade="all, delete-orphan"
    )
    subjects = db.relationship(
        "Subject",
        back_populates="school",
        cascade="all, delete-orphan"
    )
    academic_records = db.relationship(
        "AcademicRecord",
        back_populates="school",
        lazy=True,
        cascade="all, delete-orphan"    
    )
    academic_sessions = db.relationship(
    "AcademicSession",
    back_populates="school",
    cascade="all, delete-orphan",
    lazy=True
    )
    reports = db.relationship(
        "Report",
        back_populates="school",
        lazy=True,
        cascade="all, delete-orphan"
    )
    behaviours = db.relationship(
        "Behaviour",
        back_populates="school",
        lazy=True,
        cascade="all, delete-orphan"
    )
    attendance_records = db.relationship(
        "Attendance",
        back_populates="school",
        lazy=True,
        cascade="all, delete-orphan"
    )
    notifications = db.relationship(
        "Notification",
        back_populates="school",
        lazy=True,
        cascade="all, delete-orphan"
    )
    
    activities = db.relationship(
    "Activity",
    back_populates="school",
    lazy=True,
    cascade="all, delete-orphan"
    )

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return f"<School {self.name}>"