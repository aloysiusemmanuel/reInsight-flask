"""
=========================================================
Teacher Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class Teacher(BaseModel, db.Model):
    """
    Represents a teacher in a school.
    """

    __tablename__ = "teachers"

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
        back_populates="teachers"
    )
    
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )
    
    user = db.relationship(
    "User",
    back_populates="teacher"
    )
    
    #=====================================================
    # RELATIONSHIPS
    #=====================================================
    subjects = db.relationship(
        "Subject",
        secondary="teacher_subjects",
        back_populates="teachers",
        lazy="dynamic"
    )
    
    subject_assignments = db.relationship(
    "ClassSubjectAssignment",
    back_populates="teacher",
    cascade="all, delete-orphan"
    )
    academic_records = db.relationship(
        "AcademicRecord",
        back_populates="teacher",
        lazy=True
    )
    reports = db.relationship(
        "Report",
        back_populates="teacher",
        lazy=True
    )
    classrooms = db.relationship(
        "Classroom",
        secondary="teacher_classrooms",
        back_populates="class_teacher",
        lazy=True
    )
    subjects = db.relationship(
        "Subject",
        secondary="teacher_subjects",
        back_populates="teacher",
        lazy=True
    )
    behaviours = db.relationship(
        "Behaviour",
        back_populates="teacher",
        lazy=True
    )
    attendance_records = db.relationship(
        "Attendance",
        back_populates="teacher",
        lazy=True   
    )
    notifications = db.relationship(
        "Notification",
        back_populates="teacher",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # =====================================================
    # EMPLOYMENT INFORMATION
    # =====================================================

    employment_date = db.Column(
        db.Date,
        nullable=True
    )

    employment_type = db.Column(
        db.String(30),
        default="Full Time"
    )

    department = db.Column(
        db.String(100),
        nullable=True
    )

    designation = db.Column(
        db.String(100),
        nullable=True
    )

    qualification = db.Column(
        db.String(150),
        nullable=True
    )

    years_of_experience = db.Column(
        db.Integer,
        default=0
    )
    
    salary_grade = db.Column(
        db.String(30)
    )

    is_class_teacher = db.Column(
        db.Boolean,
        default=False
    )

    status = db.Column(
        db.String(20),
        default="Active"
    )

    # =====================================================
    # PERSONAL INFORMATION
    # =====================================================
    staff_id = db.Column(
        db.String(30),
        unique=True,
        nullable=False
    )

    title = db.Column(
        db.String(20)
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
        nullable=True
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )
    
    marital_status = db.Column(
        db.String(30)
    )

    phone = db.Column(
        db.String(20),
        nullable=False
    )

    address = db.Column(
        db.Text,
        nullable=True
    )

    photo = db.Column(
        db.String(255),
        nullable=True
    )

    # =====================================================
    # QUALIFICATIONS
    # =====================================================

    highest_qualification = db.Column(
        db.String(120)
    )

    institution = db.Column(
        db.String(150)
    )

    graduation_year = db.Column(
        db.Integer
    )

    specialization = db.Column(
        db.String(150)
    )

    certification = db.Column(
        db.String(255)
    )
    
    # =====================================================
    # CONTACT INFORMATION
    # =====================================================

    phone = db.Column(
        db.String(20)
    )

    alternate_phone = db.Column(
        db.String(20)
    )

    email = db.Column(
        db.String(120),
        unique=True
    )

    address = db.Column(
        db.Text
    )

    emergency_contact = db.Column(
        db.String(120)
    )

    emergency_phone = db.Column(
        db.String(20)
    )

    # =====================================================
    # HELPER PROPERTIES
    # =====================================================

    @property
    def full_name(self):
        names = [
            self.title,
            self.first_name,
            self.other_name,
            self.last_name
        ]

        return " ".join(filter(None, names))

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return f"<Teacher {self.staff_id} - {self.full_name}>"