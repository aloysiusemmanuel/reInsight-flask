"""
=========================================================
User Model
=========================================================

Central authentication model for the reInsight SaaS
platform.

Every person who can log into the system has one User
account.

Roles include:
    - SUPER_ADMIN
    - SCHOOL_ADMIN
    - TEACHER
    - PARENT
"""

from datetime import datetime

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask_login import UserMixin

from packages.extensions import db
from .base import BaseModel


class User(UserMixin, BaseModel, db.Model):
    """
    Central authentication model.
    """

    __tablename__ = "users"

    # =====================================================
    # SCHOOL
    # =====================================================

    school_id = db.Column(
        db.Integer,
        db.ForeignKey("schools.id"),
        nullable=True,
        index=True
    )
    # Nullable because SUPER_ADMIN does not belong to
    # any school.

    # =====================================================
    # ROLE
    # =====================================================

    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
        nullable=False,
        index=True
    )

    # =====================================================
    # LOGIN INFORMATION
    # =====================================================

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False,
        index=True
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    # =====================================================
    # ACCOUNT STATUS
    # =====================================================

    email_verified = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )
    
    is_active = db.Column(
    db.Boolean,
    default=True,
    nullable=False
    )

    is_locked = db.Column(
        db.Boolean,
        default=False,
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

    # =====================================================
    # RELATIONSHIPS
    # =====================================================

    school = db.relationship(
        "School",
        back_populates="users"
    )

    role = db.relationship(
        "Role",
        back_populates="users"
    )

    school_admin = db.relationship(
        "SchoolAdmin",
        back_populates="user",
        uselist=False
    )

    teacher = db.relationship(
        "Teacher",
        back_populates="user",
        uselist=False
    )

    parent = db.relationship(
        "Parent",
        back_populates="user",
        uselist=False
    )

    # =====================================================
    # PASSWORD METHODS
    # =====================================================

    def set_password(self, password):
        """
        Hash and save a password.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verify password.
        """
        return check_password_hash(
            self.password_hash,
            password
        )

    # =====================================================
    # LOGIN METHODS
    # =====================================================

    def record_successful_login(self):
        """
        Reset failed attempts and update login time.
        """
        self.failed_login_attempts = 0
        self.last_login = datetime.utcnow()

    def record_failed_login(self):
        """
        Increase failed login attempts.
        """
        self.failed_login_attempts += 1

        if self.failed_login_attempts >= 5:
            self.is_locked = True

    # =====================================================
    # ROLE HELPERS
    # =====================================================

    @property
    def role_name(self):
        if self.role:
            return self.role.name
        return None

    @property
    def is_super_admin(self):
        return self.role_name == "SUPER_ADMIN"

    @property
    def is_school_admin(self):
        return self.role_name == "SCHOOL_ADMIN"

    @property
    def is_teacher(self):
        return self.role_name == "TEACHER"

    @property
    def is_parent(self):
        return self.role_name == "PARENT"

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return (
            f"<User {self.username} "
            f"({self.role_name})>"
        )