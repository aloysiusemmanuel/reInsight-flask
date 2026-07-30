"""
=========================================================
Role Model
=========================================================

Defines the different user roles within the reInsight
SaaS platform.

Examples:
    - SUPER_ADMIN
    - SCHOOL_ADMIN
    - TEACHER
    - PARENT
"""

from packages.extensions import db
from .base import BaseModel


class Role(BaseModel, db.Model):
    """
    Represents a system role.

    Each User belongs to one Role.
    """

    __tablename__ = "roles"

    # =====================================================
    # ROLE INFORMATION
    # =====================================================

    name = db.Column(
        db.String(50),
        unique=True,
        nullable=False,
        index=True
    )

    description = db.Column(
        db.String(255),
        nullable=True
    )

    is_system = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )
    # True = Cannot be deleted
    # False = Custom role created by a school (future feature)

    # =====================================================
    # RELATIONSHIPS
    # =====================================================

    users = db.relationship(
        "User",
        back_populates="role",
        lazy=True
    )

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return f"<Role {self.name}>"

    # =====================================================
    # HELPER METHODS
    # =====================================================

    @property
    def display_name(self):
        """
        Returns a human-readable role name.

        Example:
            SCHOOL_ADMIN -> School Admin
        """
        return self.name.replace("_", " ").title()