import os

from flask import Flask, render_template, request, redirect

from .extensions import db, migrate
from .models.carbon_calculation import CarbonCalculation
from .models.default_values import DefaultValues

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

    @app.route("/")
    @app.route("/index", methods=['POST', 'GET'])
    def index():
        
        if request.method == 'POST':
            new_calculation = CarbonCalculation(str(request.form['session_name']), float(request.form['required_area']), int(request.form['amount_layers']), DefaultValues)

            get_result = new_calculation.calculate
            session_name = new_calculation.session_name
            area = get_result()['area']
            resin = get_result()['resin']
            hardner = get_result()['hardner']
            cost = get_result()['cost']


            return render_template("index.html", session_name=session_name, area=area, resin=resin, hardner=hardner, cost=cost)
        else:
            return render_template("index.html")
        
    @app.route("/defaults", methods=['POST', 'GET'])
    def defaults():
        # def insert_dummy_data():
        #     insert_data = Default_values(resin_type = "Some resin type", resin_weight = 1.5, 
        #                             price_resin = 2.0, hardner_type = "Some hardner type", price_hardner = 6.0, hardner_weight = 0.5, 
        #                             resin_ratio = 2, hardner_ratio = 1, extra_resin_percent = 20, carbon_type = "3K", default_carbon_size_width = 1,
        #                             default_carbon_size_height = 1, default_carbon_weight = 200, price_carbon = 50.0)
        #     db.session.add(insert_data)
        #     db.session.commit()

        get_default_values = DefaultValues.query.first()
        if request.method == 'POST':
            get_default_values.resin_type = request.form['resin_type']
            get_default_values.resin_weight = request.form['resin_weight']
            get_default_values.price_resin = request.form['price_resin']
            get_default_values.hardner_type = request.form['hardner_type']
            get_default_values.price_hardner = request.form['price_hardner']
            get_default_values.hardner_weight = request.form['hardner_weight']
            get_default_values.resin_ratio = request.form['resin_ratio']
            get_default_values.hardner_ratio = request.form['hardner_ratio']
            get_default_values.extra_resin_percent = request.form['extra_resin_percent']
            get_default_values.carbon_type = request.form['carbon_type']
            get_default_values.default_carbon_size_width = request.form['default_carbon_size_width']
            get_default_values.default_carbon_size_height = request.form['default_carbon_size_height']
            get_default_values.default_carbon_weight = request.form['default_carbon_weight']
            get_default_values.price_carbon = request.form['price_carbon']

            try:
                db.session.commit()
                return redirect('/defaults')
            except:
                return 'A error occurred'
        else:
            return render_template('defaults.html', get_default_values=get_default_values)

    return app