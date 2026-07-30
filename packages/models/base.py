"""
=========================================================
Base Model
Shared fields inherited by all models.
=========================================================
"""

from datetime import datetime
from sqlalchemy.sql import func
from packages.extensions import db


class BaseModel:
    """
    Abstract base model for all database models.
    """

    __abstract__ = True

    # =====================================================
    # PRIMARY KEY
    # =====================================================

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # =====================================================
    # STATUS
    # =====================================================

    is_active = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    # =====================================================
    # AUDIT FIELDS
    # =====================================================

    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    # =====================================================
    # SOFT DELETE
    # =====================================================

    deleted_at = db.Column(
        db.DateTime,
        nullable=True
    )

    # =====================================================
    # HELPER METHODS
    # =====================================================

    def soft_delete(self):
        """Soft delete the record."""
        self.deleted_at = datetime.utcnow()
        self.is_active = False

    def restore(self):
        """Restore a soft deleted record."""
        self.deleted_at = None
        self.is_active = True

    def save(self):
        """Save current object."""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Permanently delete current object."""
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"