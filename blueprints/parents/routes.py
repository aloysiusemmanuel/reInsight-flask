from flask import render_template, url_for



from . import parents_bp



# ==========================================================
# PARENTS
# ==========================================================

@parents_bp.route("/", endpoint="parents_home")
def parents():
    return render_template("parents/parents_home.html",
                           
    
        page_title="Parent Management",
        page_subtitle="Manage parent and guardian records linked to students.",
        
        page_icon="bi bi-person-workspace",
                     
        breadcrumbs=[
            {"title":"Dashboard","url":url_for("dashboard.dashboard")},
            {"title":"Parents"}
                     
                    ],                     
        primary_button={
            "text":"Add Parent",
            "icon":"bi bi-plus-circle",
            "url":url_for("parents.parent_create")
                      }                               
    )

@parents_bp.route("/create", endpoint="parent_create")
def parent_create():
    return render_template("parents/parent_create.html")