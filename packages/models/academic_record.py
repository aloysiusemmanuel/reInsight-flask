"""
=========================================================
Academic Record Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class AcademicRecord(BaseModel, db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    """
    Stores the academic performance of a student
    for a particular subject.
    """

    __tablename__ = "academic_records"

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
        nullable=False,
        index=True
    )

    classroom_id = db.Column(
        db.Integer,
        db.ForeignKey("classrooms.id"),
        nullable=False,
        index=True
    )

    subject_id = db.Column(
        db.Integer,
        db.ForeignKey("subjects.id"),
        nullable=False,
        index=True
    )

    teacher_id = db.Column(
        db.Integer,
        db.ForeignKey("teachers.id"),
        nullable=False,
        index=True
    )

    school = db.relationship(
        "School",
        back_populates="academic_records"
    )

    student = db.relationship(
        "Student",
        back_populates="academic_records"
    )

    classroom = db.relationship(
        "Classroom",
        back_populates="academic_records"
    )

    subject = db.relationship(
        "Subject",
        back_populates="academic_records"
    )

    teacher = db.relationship(
        "Teacher",
        back_populates="academic_records"
    )

    # =====================================================
    # ACADEMIC SESSION
    # =====================================================

    academic_session = db.Column(
        db.String(20),
        nullable=False
    )

    term = db.Column(
        db.String(20),
        nullable=False
    )

    # =====================================================
    # CONTINUOUS ASSESSMENT
    # =====================================================

    assignment = db.Column(
        db.Float,
        default=0
    )

    class_test = db.Column(
        db.Float,
        default=0
    )

    project = db.Column(
        db.Float,
        default=0
    )

    practical = db.Column(
        db.Float,
        default=0
    )

    ca_score = db.Column(
        db.Float,
        default=0
    )

    # =====================================================
    # EXAMINATION
    # =====================================================

    exam_score = db.Column(
        db.Float,
        default=0
    )

    # =====================================================
    # FINAL RESULT
    # =====================================================

    total_score = db.Column(
        db.Float,
        default=0
    )

    grade = db.Column(
        db.String(5),
        nullable=True
    )

    remark = db.Column(
        db.String(100),
        nullable=True
    )

    position = db.Column(
        db.Integer,
        nullable=True
    )

    # =====================================================
    # COMMENTS
    # =====================================================

    teacher_comment = db.Column(
        db.Text,
        nullable=True
    )

    principal_comment = db.Column(
        db.Text,
        nullable=True
    )

    # =====================================================
    # STATUS
    # =====================================================

    published = db.Column(
        db.Boolean,
        default=False
    )
    
    submission_status = db.Column(
    db.String(20),
    default="Draft"
    )

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return (
            f"<AcademicRecord "
            f"{self.student.full_name} - "
            f"{self.subject.name}>"
        )