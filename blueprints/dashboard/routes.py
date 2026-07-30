from flask import render_template, url_for

from . import dashboard_bp


# ======================================================
# Dashboard
# ======================================================

@dashboard_bp.route("/", endpoint="dashboard")
def dashboard():
    return render_template("dashboard/dashboard.html")

@dashboard_bp.route("/dasboard_base", endpoint="dashboard_base")
def dasboard_base():
    return render_template("dashboard/dasboard_base.html")

@dashboard_bp.route("/dashboard_sidebar", endpoint="sidebar")
def sidebar():
    return render_template("dashboard/sidebar.html")

@dashboard_bp.route("/dashboard_footer", endpoint="footer")
def footer():
    return render_template("dashboard/footer.html")

@dashboard_bp.route("/dashboard_navbar", endpoint="navbar")
def navbar():
    return render_template("dashboard/navbar.html")

@dashboard_bp.route("/analytics", endpoint="analytics")
def analytics():

    return render_template(

        "dashboard/analytics.html",

        page_title="Analytics",

        page_description="Analyse trends and gain actionable insights from your school data.",

        page_icon="bi bi-bar-chart-line-fill",

        breadcrumbs=[
            {"title":"Dashboard","url":url_for("dashboard.dashboard")},
            {"title":"Analytics"}
        ],

        primary_button={
            "text":"Export Analytics",
            "icon":"bi bi-download",
            "url":"#"
        }

    )


@dashboard_bp.route("/reports", endpoint="reports")
def reports():

    return render_template(

        "dashboard/reports.html",

        page_title="Reports",

        page_description="Generate and manage school reports.",

        page_icon="bi bi-file-earmark-bar-graph-fill",

        breadcrumbs=[
            {"title":"Dashboard","url":url_for("dashboard.dashboard")},
            {"title":"Reports"}
        ],

        primary_button={
            "text":"Generate Report",
            "icon":"bi bi-plus-circle",
            "url":"#"
        }

    )



@dashboard_bp.route("/profile", endpoint="profile")
def profile():

    return render_template(

        "dashboard/profile.html",

        page_title="My Profile",

        page_description="View and manage your administrator account.",

        page_icon="bi bi-person-circle",

        breadcrumbs=[
            {"title":"Dashboard","url":url_for("dashboard.dashboard")},
            {"title":"My Profile"}
        ],

        primary_button={
            "text":"Settings",
            "icon":"bi bi-gear-fill",
            "url":url_for("settings")
        },

        user=None

    )
    
@dashboard_bp.route("/settings", endpoint="settings")
def settings():

    return render_template(

        "dashboard/settings.html",

        page_title="Settings",

        page_description="Configure your school and account preferences.",

        page_icon="bi bi-gear-fill",

        breadcrumbs=[
            {"title":"Dashboard","url":url_for("dashboard.dashboard")},
            {"title":"Settings"}
        ]

    )
    