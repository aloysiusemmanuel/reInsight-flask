from flask import render_template, redirect, request, flash, url_for

from . import public_bp






# ======================================================
# Public Website Routes
# ======================================================

@public_bp.route("/")
def index():
    return render_template("index.html")


@public_bp.route("/about")
def about():
    return render_template("about.html")


@public_bp.route("/features")
def features():
    return render_template("features.html")


@public_bp.route("/pricing")
def pricing():
    return render_template("pricing.html")


@public_bp.route("/faq")
def faq():
    return render_template("faq.html")


@public_bp.route("/demo", methods=["GET", "POST"])
def demo():
    return render_template("demo.html")

# ======================================================
# Contact
# ======================================================

@public_bp.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip()
        school = request.form.get("school_name", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        if not name:
            flash("Full name is required.", "danger")
            return redirect(url_for("public.contact"))

        if not email:
            flash("Email address is required.", "danger")
            return redirect(url_for("public.contact"))

        if not school:
            flash("School name is required.", "danger")
            return redirect(url_for("public.contact"))

        if not subject:
            flash("Subject is required.", "danger")
            return redirect(url_for("public.contact"))

        if not message:
            flash("Message is required.", "danger")
            return redirect(url_for("public.contact"))

        flash("Thank you. Your message has been received.", "success")

        return redirect(url_for("public.contact"))

    return render_template("contact.html")

