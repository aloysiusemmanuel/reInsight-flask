"""
=========================================================
Activity Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class Activity(BaseModel, db.Model):
    """
    Stores important activities performed within a school.
    """

    __tablename__ = "activities"

    # =====================================================
    # SCHOOL
    # =====================================================

    school_id = db.Column(
        db.Integer,
        db.ForeignKey("schools.id"),
        nullable=False,
        index=True
    )

    school = db.relationship(
        "School",
        back_populates="activities"
    )

    # =====================================================
    # USER
    # =====================================================

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True,
        index=True
    )

    user = db.relationship(
        "User",
        back_populates="activities"
    )

    # =====================================================
    # ACTIVITY INFORMATION
    # =====================================================

    action = db.Column(
        db.String(50),
        nullable=False
    )

    description = db.Column(
        db.String(255),
        nullable=False
    )

    entity_type = db.Column(
        db.String(50),
        nullable=True
    )

    entity_id = db.Column(
        db.Integer,
        nullable=True
    )

    icon = db.Column(
        db.String(100),
        nullable=True
    )

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):

        return (
            f"<Activity {self.action}>"
        )