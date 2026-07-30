from flask import render_template

from . import behaviour_bp



# ==========================================================
# BEHAVIOUR MODULE | The @login_required will be added during authentication
# ==========================================================

@behaviour_bp.route("/", endpoint="behaviour_home")
# @login_required
def behaviour_home():
    """
    Behaviour dashboard.
    """
    return render_template("behaviour/behaviour_home.html")


@behaviour_bp.route("/create", endpoint="behaviour_create", methods=["GET", "POST"])
# @login_required
def behaviour_create():
    """
    Record a new behaviour incident.
    """
    return render_template("behaviour/behaviour_create.html")


@behaviour_bp.route("/profile/<int:behaviour_id>", endpoint="behaviour_profile")
# @login_required
def behaviour_profile(behaviour_id):
    """
    View a behaviour record.
    """
    return render_template(
        "behaviour/behaviour_profile.html",
        behaviour_id=behaviour_id
    )


@behaviour_bp.route("/edit/<int:behaviour_id>", endpoint="behaviour_edit", methods=["GET", "POST"])
# @login_required
def behaviour_edit(behaviour_id):
    """
    Edit a behaviour record.
    """
    return render_template(
        "behaviour/behaviour_edit.html",
        behaviour_id=behaviour_id
    )


@behaviour_bp.route("/reports", endpoint="behaviour_reports")
# @login_required
def behaviour_reports():
    """
    Behaviour reports.
    """
    return render_template("behaviour/behaviour_reports.html")


@behaviour_bp.route("/analytics", endpoint="behaviour_analytics")
# @login_required
def behaviour_analytics():
    """
    Behaviour analytics.
    """
    return render_template("behaviour/behaviour_analytics.html")

# ==========================================================
# BEHAVIOUR CATEGORY MODULE
# ==========================================================

@behaviour_bp.route("/categories", endpoint="behaviour_categories_home")
# @login_required
def behaviour_category_home():
    """
    List behaviour categories.
    """
    return render_template("behaviour/categories/category_home.html")


@behaviour_bp.route("/categories/create", endpoint="behaviour_category_create", methods=["GET", "POST"])
# @login_required
def behaviour_category_create():
    """
    Create a behaviour category.
    """
    return render_template("behaviour/categories/category_create.html")


@behaviour_bp.route("/categories/<int:category_id>", endpoint="behaviour_category_profile")
# @login_required
def behaviour_category_profile(category_id):
    """
    View behaviour category.
    """
    return render_template(
        "behaviour/categories/category_profile.html",
        category_id=category_id
    )


@behaviour_bp.route("/categories/<int:category_id>/edit", endpoint="behaviour_category_edit", methods=["GET", "POST"])
# @login_required
def behaviour_category_edit(category_id):
    """
    Edit behaviour category.
    """
    return render_template(
        "behaviour/categories/category_edit.html",
        category_id=category_id
    )
