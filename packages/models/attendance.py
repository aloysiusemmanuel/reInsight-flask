"""
=========================================================
Attendance Model
=========================================================
"""

from packages.extensions import db
from .base import BaseModel


class Attendance(BaseModel, db.Model):
    """
    Stores a student's daily attendance record.
    """

    __tablename__ = "attendance"
    
    __table_args__ = (
        db.UniqueConstraint(
            "student_id",
            "attendance_date",
            name="uq_student_attendance_date"
        ),
    )

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

    teacher_id = db.Column(
        db.Integer,
        db.ForeignKey("teachers.id"),
        nullable=False,
        index=True
    )

    school = db.relationship(
        "School",
        back_populates="attendance_records"
    )

    student = db.relationship(
        "Student",
        back_populates="attendance_records"
    )

    classroom = db.relationship(
        "Classroom",
        back_populates="attendance_records"
    )

    teacher = db.relationship(
        "Teacher",
        back_populates="attendance_records"
    )

    # =====================================================
    # ACADEMIC PERIOD
    # =====================================================

    academic_session = db.Column(
        db.String(20),
        nullable=False
    )

    term = db.Column(
        db.String(20),
        nullable=False
    )

    submission_status = db.Column(
    db.String(20),
    default="Draft"
)
    # =====================================================
    # ATTENDANCE
    # =====================================================

    attendance_date = db.Column(
        db.Date,
        nullable=False,
        index=True
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Present"
    )
    # Present
    # Absent
    # Late
    # Excused

    check_in_time = db.Column(
        db.Time,
        nullable=True
    )

    check_out_time = db.Column(
        db.Time,
        nullable=True
    )

    # =====================================================
    # REASON
    # =====================================================

    absence_reason = db.Column(
        db.Text,
        nullable=True
    )

    remarks = db.Column(
        db.Text,
        nullable=True
    )

    parent_notified = db.Column(
        db.Boolean,
        default=False
    )

    # =====================================================
    # REPRESENTATION
    # =====================================================

    def __repr__(self):
        return (
            f"<Attendance "
            f"{self.student.full_name} "
            f"{self.attendance_date}>"
        )