from packages.models.academic_session import AcademicSession
from packages.models.term import Term


def get_active_academic_period(school_id):
    """
    Get the currently active academic session and term
    for a particular school.

    Returns:
        tuple:
            (active_session, active_term)
    """

    active_session = (
        AcademicSession.query
        .filter_by(
            school_id=school_id,
            is_active=True
        )
        .first()
    )

    if not active_session:
        return None, None

    active_term = (
        Term.query
        .filter_by(
            academic_session_id=active_session.id,
            is_active=True
        )
        .first()
    )

    return active_session, active_term