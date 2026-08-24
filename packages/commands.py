import click

from flask import current_app
from flask.cli import with_appcontext

from packages.extensions import db
from packages.models.user import User
from packages.models.role import Role


@click.command("seed-roles")
def seed_roles():

    roles = [
        {
            "name": "SUPER_ADMIN",
            "description": "System-wide administrator with full access.",
            "is_system": True
        },
        {
            "name": "SCHOOL_ADMIN",
            "description": "Administrator responsible for managing a school.",
            "is_system": True
        },
        {
            "name": "TEACHER",
            "description": "Teacher responsible for teaching and managing academic activities.",
            "is_system": True
        },
        {
            "name": "PARENT",
            "description": "Parent or guardian who can monitor student information.",
            "is_system": True
        },
        {
            "name": "STUDENT",
            "description": "Student with access to permitted academic information.",
            "is_system": True
        }
    ]

    created = 0

    for role_data in roles:

        existing_role = Role.query.filter_by(
            name=role_data["name"]
        ).first()

        if existing_role:
            click.echo(
                f"Role already exists: {role_data['name']}"
            )
            continue

        role = Role(
            name=role_data["name"],
            description=role_data["description"],
            is_system=role_data["is_system"]
        )

        db.session.add(role)

        click.echo(
            f"Created role: {role_data['name']}"
        )

        created += 1

    db.session.commit()

    click.echo(
        f"Role seeding completed. {created} role(s) created."
    )

@click.command("seed-superadmin")
@with_appcontext
def seed_superadmin():

    # -------------------------------------------------
    # Find SUPER_ADMIN role
    # -------------------------------------------------

    role = Role.query.filter_by(
        name="SUPER_ADMIN"
    ).first()

    if not role:

        click.echo(
            "SUPER_ADMIN role does not exist."
        )

        return

    # -------------------------------------------------
    # Check if Super Admin already exists
    # -------------------------------------------------

    existing_user = User.query.filter_by(
        role_id=role.id
    ).first()

    if existing_user:

        click.echo(
            f"Super Admin already exists: "
            f"{existing_user.username}"
        )

        return

    # -------------------------------------------------
    # Create Super Admin
    # -------------------------------------------------

    user = User(
        username="superadmin",
        email="admin@reinsight.com",
        role_id=role.id,
        school_id=None,
        email_verified=True,
        is_active=True,
        is_locked=False
    )

    user.set_password("Admin@12345")

    db.session.add(user)
    db.session.commit()

    click.echo(
        "Super Admin created successfully."
    )

    click.echo(
        "Username: superadmin"
    )

    click.echo(
        "Password: Admin@12345"
    )