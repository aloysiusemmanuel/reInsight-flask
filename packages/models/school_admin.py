"""
=========================================================
School Administrator Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class SchoolAdmin(BaseModel, db.Model):
    """
    Represents the administrator of a school.
    """

    __tablename__ = "school_admins"

    # =====================================================
    # SCHOOL RELATIONSHIP
    # =====================================================

    school_id = db.Column(
        db.Integer,
        db.ForeignKey("schools.id"),
        nullable=False,
        index=True
    )
    
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True,
        index=True
    )
    
    user = db.relationship(
        "User", back_populates="school_admin"
    )
    
    school = db.relationship(
        "School",
        back_populates="administrators"
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

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )

    phone = db.Column(
        db.String(20),
        nullable=True
    )

    photo = db.Column(
        db.String(255),
        nullable=True
    )

    gender = db.Column(
        db.String(20),
        nullable=True
    )

    # =====================================================
    # ACCOUNT STATUS
    # =====================================================

    email_verified = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    first_login = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    failed_login_attempts = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )

    last_login = db.Column(
        db.DateTime,
        nullable=True
    )

    password_changed_at = db.Column(
        db.DateTime,
        nullable=True
    )
    password_hash = db.Column(
        db.String(255), 
        nullable=False
        )

    # =====================================================
    # REPRESENTATION
    # =====================================================

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<SchoolAdmin {self.full_name}>"