"""
=========================================================
reInsight Models Package
=========================================================

This package contains all SQLAlchemy models used
throughout the reInsight application.
"""
from .base import BaseModel
from .classroom import Classroom

# Core Models
from .school import School
from .school_admin import SchoolAdmin
from .teacher import Teacher
from .parent import Parent
from .student import Student

# Auth Models
from .role import Role
from .user import User


# Academic Models
from .subject import Subject
from .attendance import Attendance
from .academic_record import AcademicRecord
from .behaviour import Behaviour
from .report import Report
from .notification import Notification
from .association import teacher_classrooms, teacher_subjects
from .class_subject_assignment import ClassSubjectAssignment
from .academic_session import AcademicSession
from .term import Term
from .lesson_note import LessonNote

__all__ = [
    "BaseModel",
    "School",
    "SchoolAdmin",
    "Teacher",
    "Parent",
    "Student",
    "Classroom",
    "Subject",
    "AcademicRecord",
    "Report",
    "Behaviour",
    "Attendance",
    "Notification",
    teacher_subjects,
    teacher_classrooms,
    "ClassSubjectAssignment",
    "AcademicSession",
    "Term",
    "Role",
    "User",
    "LessonNote"
]