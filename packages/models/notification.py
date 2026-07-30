"""
=========================================================
Notification Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class Notification(BaseModel, db.Model):
    """
    Stores notifications sent by the system.
    """

    __tablename__ = "notifications"

    # =====================================================
    # RELATIONSHIPS
    # =====================================================

    school_id = db.Column(
        db.Integer,
        db.ForeignKey("schools.id"),
        nullable=False,
        index=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=True,
        index=True
    )

    parent_id = db.Column(
        db.Integer,
        db.ForeignKey("parents.id"),
        nullable=True,
        index=True
    )

    teacher_id = db.Column(
        db.Integer,
        db.ForeignKey("teachers.id"),
        nullable=True,
        index=True
    )

    school = db.relationship(
        "School",
        back_populates="notifications"
    )

    parent = db.relationship(
        "Parent",
        back_populates="notifications"
    )

    teacher = db.relationship(
        "Teacher",
        back_populates="notifications"
    )

    # =====================================================
    # NOTIFICATION DETAILS
    # =====================================================

    title = db.Column(
        db.String(200),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=False
    )
    # Attendance
    # Behaviour
    # Academic
    # Announcement
    # Reminder
    # Fee
    # General

    notification_type = db.Column(
        db.String(30),
        nullable=False,
        default="In-App"
    )
    # In-App
    # Email
    # SMS
    # Push
    # WhatsApp

    priority = db.Column(
        db.String(20),
        default="Normal"
    )
    # Low
    # Normal
    # High
    # Critical

    # =====================================================
    # STATUS
    # =====================================================

    is_read = db.Column(
        db.Boolean,
        default=False
    )

    is_sent = db.Column(
        db.Boolean,
        default=False
    )

    sent_at = db.Column(
        db.DateTime,
        nullable=True
    )

    read_at = db.Column(
        db.DateTime,
        nullable=True
    )

    # =====================================================
    # OPTIONAL LINK
    # =====================================================

    action_url = db.Column(
        db.String(255),
        nullable=True
    )

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return (
            f"<Notification "
            f"{self.title}>"
        )