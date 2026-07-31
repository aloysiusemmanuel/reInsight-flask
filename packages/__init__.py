from flask import Flask
from instance.config import Config

from packages.extensions import db, migrate, login_manager
from packages.authentication import auth_bp
from datetime import datetime

from blueprints.public import public_bp
from blueprints.dashboard import dashboard_bp
from blueprints.students import students_bp
from blueprints.teachers import teachers_bp
from blueprints.classrooms import classrooms_bp
from blueprints.attendance import attendance_bp
from blueprints.academics import academics_bp
from blueprints.behaviour import behaviour_bp
from blueprints.parents import parents_bp
from blueprints.superadmin import superadmin_bp
from blueprints.teacher_dashboard import teacher_dash_bp
from blueprints.parent_dashboard import parent_dash_bp



def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(teachers_bp)
    app.register_blueprint(classrooms_bp)
    app.register_blueprint(attendance_bp)
    app.register_blueprint(academics_bp)
    app.register_blueprint(behaviour_bp)
    app.register_blueprint(parents_bp)
    app.register_blueprint(superadmin_bp)
    app.register_blueprint(teacher_dash_bp)
    app.register_blueprint(parent_dash_bp)
    
    
    @app.context_processor
    def inject_global_variables():
        return {
            "current_year": datetime.now().year
        }

    return app


app = create_app()