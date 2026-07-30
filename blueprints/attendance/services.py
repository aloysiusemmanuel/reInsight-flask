from packages.models.attendance import Attendance


def get_student_attendance(student_id):

    return Attendance.query.filter_by(
        student_id=student_id).order_by(Attendance.date.desc()).all()


def attendance_summary(student_id):

    records = Attendance.query.filter_by(student_id=student_id).all()

    total = len(records)

    present = sum(1 for r in records if r.status == "Present")
    absent = sum(1 for r in records if r.status == "Absent")
    late = sum(1 for r in records if r.status == "Late")

    percentage = round((present / total) * 100, 1) if total else 0

    return {
        "total": total,
        "present": present,
        "absent": absent,
        "late": late,
        "percentage": percentage
    }