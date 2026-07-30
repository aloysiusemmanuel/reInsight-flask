from flask import render_template, redirect, session, request, flash, url_for



from . import teachers_bp


# ==========================================================
# TEACHERS
# ==========================================================

@teachers_bp.route("/", endpoint="teachers_home")
def teachers_home():
    return render_template("teachers/teachers_home.html"
    ,

    page_title="Teachers",

    page_description="Manage teachers and staff.",

    page_icon="bi bi-person-workspace",

    breadcrumbs=[

        {"title":"Dashboard","url":url_for("dashboard.dashboard")},

        {"title":"Teachers"}

    ],

    primary_button={

        "text":"Add Teacher",

        "icon":"bi bi-plus-circle",

        "url":url_for("teachers.teacher_create")

    }                    
    )


@teachers_bp.route("/create", endpoint="teacher_create")
def teacher_create():
    return render_template("teachers/teachers_create.html",   
                           
        page_title="Teachers",
    
        page_description="Manage teachers and staff.",
    
        page_icon="bi bi-person-workspace",
    
        breadcrumbs=[
    
            {"title":"Dashboard","url":url_for("dashboard.dashboard")},
    
            {"title":"Teachers"}
    
        ],    
        primary_button={
        
                "text":"Add Teacher",
        
                "icon":"bi bi-plus-circle",
        
                "url":url_for("teachers.teacher_create")
        
            } 
                           
                           
                           )


@teachers_bp.route("/profile/<int:teacher_id>", endpoint="teacher_profile")
def teachers_profile(teacher_id):
    return render_template(
        "teachers/profile.html",
        teacher_id=teacher_id
    )

from . import routes