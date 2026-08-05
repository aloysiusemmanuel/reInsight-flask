from packages.extensions import db
from datetime import datetime
from .base import BaseModel


class LessonNote(BaseModel, db.Model):
    
    __tablename__ = "lesson_notes"
    id = db.Column(db.Integer, primary_key=True)

    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"), nullable=False)
    classroom_id = db.Column(db.Integer, db.ForeignKey("classrooms.id"), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)

    week = db.Column(db.Integer, nullable=False)
    topic = db.Column(db.String(200), nullable=False)
    duration = db.Column(db.String(50))

    objectives = db.Column(db.Text)
    prior_knowledge = db.Column(db.Text)
    instructional_materials = db.Column(db.Text)
    presentation_steps = db.Column(db.Text)
    evaluation = db.Column(db.Text)
    assignment = db.Column(db.Text)

    ai_generated = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime)
    
    updated_at = db.Column(db.DateTime, default=datetime, onupdate=datetime)
    
    classroom = db.relationship("Classroom", backref="lesson_notes")