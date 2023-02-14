import os

from flask import Flask, render_template, request, redirect

from .extensions import db, migrate
from .models.carbon_calculation import CarbonCalculation
from .models.default_values import DefaultValues
from .routes import main


def create_app(test_config=None):

    basedir = os.path.abspath(os.path.dirname(__file__))
    app     = Flask(__name__,
                    template_folder = basedir + '/templates',
                    static_folder = basedir + '/static')

    # Setup database connection
    app.config['SECRET_KEY'] = 'SomeKey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Init app section
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main, url_prefix='')

    return app