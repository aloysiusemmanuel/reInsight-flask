"""
=========================================================
Parent Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class Parent(BaseModel, db.Model):
    """
    Represents a parent or guardian of one or more students.
    """

    __tablename__ = "parents"

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
        back_populates="parents"
    )
    
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )
    
    user = db.relationship(
    "User",
    back_populates="parent"
    )

    # =====================================================
    # PERSONAL INFORMATION
    # =====================================================

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
        nullable=True
    )

    date_of_birth = db.Column(
        db.Date,
        nullable=True
    )

    photo = db.Column(
        db.String(255),
        nullable=True
    )

    # =====================================================
    # CONTACT INFORMATION
    # =====================================================

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )

    phone = db.Column(
        db.String(20),
        nullable=False
    )

    alternate_phone = db.Column(
        db.String(20),
        nullable=True
    )

    address = db.Column(
        db.Text,
        nullable=True
    )

    occupation = db.Column(
        db.String(120),
        nullable=True
    )

    employer = db.Column(
        db.String(150),
        nullable=True
    )

    relationship_to_student = db.Column(
        db.String(50),
        default="Parent",
        nullable=False
    )

    # =====================================================
    # RELATIONSHIPS
    # =====================================================

    students = db.relationship(
        "Student",
        back_populates="parent",
        lazy=True
    )
    notifications = db.relationship(
        "Notification",
        back_populates="parent",
        lazy=True,
        cascade="all, delete-orphan"
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
        return f"<Parent {self.full_name}>"