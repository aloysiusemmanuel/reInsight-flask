"""
=========================================================
Behaviour Category Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class BehaviourCategory(BaseModel, db.Model):
    """
    Defines behaviour categories for a school.

    Examples
    --------
    Positive:
        - Leadership
        - Honesty
        - Respect
        - Teamwork

    Negative:
        - Fighting
        - Bullying
        - Lateness
        - Truancy
    """

    __tablename__ = "behaviour_categories"

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
        back_populates="behaviour_categories"
    )

    # =====================================================
    # CATEGORY INFORMATION
    # =====================================================

    name = db.Column(
        db.String(100),
        nullable=False
    )

    category_type = db.Column(
        db.String(20),
        nullable=False
    )
    # Positive
    # Negative

    severity = db.Column(
        db.String(20),
        nullable=True
    )
    # Low
    # Medium
    # High
    # Critical

    points = db.Column(
        db.Integer,
        default=0
    )

    requires_parent_notification = db.Column(
        db.Boolean,
        default=False
    )

    requires_admin_review = db.Column(
        db.Boolean,
        default=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )
    
    display_order = db.Column(
        db.Integer,
        default=0
    )

    is_active = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    # =====================================================
    # RELATIONSHIPS
    # =====================================================

    behaviours = db.relationship(
        "Behaviour",
        back_populates="category",
        lazy=True
    )

    # =====================================================
    # CONSTRAINTS
    # =====================================================

    __table_args__ = (
        db.UniqueConstraint(
            "school_id",
            "name",
            name="uq_school_behaviour_category"
        ),
    )

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return (
            f"<BehaviourCategory {self.name}>"
        )