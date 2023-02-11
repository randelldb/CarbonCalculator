import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from carbonCalculation import CarbonCalculation

basedir = os.path.abspath(os.path.dirname(__file__))
app     = Flask(__name__)

# Setup database connection
app.config['SECRET_KEY'] = 'SomeKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db      = SQLAlchemy(app)
migrate = Migrate(app, db)

class Default_values(db.Model):
    id                          = db.Column(db.Integer, primary_key=True)
    resin_type                  = db.Column(db.String(200), nullable = False)
    resin_weight                = db.Column(db.Float)
    price_resin                 = db.Column(db.Float)
    hardner_type                = db.Column(db.String(200), nullable = False)
    price_hardner               = db.Column(db.Float)
    hardner_weight              = db.Column(db.Float)
    resin_ratio                 = db.Column(db.Integer, nullable = False)
    hardner_ratio               = db.Column(db.Integer, nullable = False)
    extra_resin_percent         = db.Column(db.Integer, nullable = False)
    carbon_type                 = db.Column(db.String(200), nullable = False)
    default_carbon_size_width   = db.Column(db.Float)
    default_carbon_size_height  = db.Column(db.Float)
    default_carbon_weight       = db.Column(db.Float)
    price_carbon                = db.Column(db.Float)


# # Calculation
# def calc_amount(required_area, amount_layers):
#     get_default_setting = Default_values.query.first()
#     resin_weight = get_default_setting.resin_weight
#     price_resin = get_default_setting.price_resin
#     hardner_weight = get_default_setting.hardner_weight
#     default_carbon_area = get_default_setting.default_carbon_size_width * get_default_setting.default_carbon_size_height
#     default_carbon_weight = get_default_setting.default_carbon_weight
#     price_carbon = get_default_setting.price_carbon

#     calc_req_area = (required_area / default_carbon_area) * amount_layers
#     calc_req_resin = (calc_req_area * default_carbon_weight) / 100 * 120
#     calc_req_hardner = (calc_req_resin / 2) / 100 * 120
#     est_cost = ((calc_req_resin / resin_weight) * price_resin) + ((calc_req_hardner / hardner_weight) * price_resin) + calc_req_area * price_carbon

#     result = {
#         "area" : str(round(calc_req_area, 3)),
#         "resin" : str(round(calc_req_resin, 3)),
#         "hardner" : str(round(calc_req_hardner, 3)),
#         "cost" : str(round(est_cost, 2))
#     }

#     return result

@app.route("/")
@app.route("/index", methods=['POST', 'GET'])
def index():
	
    if request.method == 'POST':
        new_calculation = CarbonCalculation(str(request.form['session_name']), float(request.form['required_area']), int(request.form['amount_layers']))


        # session_name = str(request.form['session_name']) 
        # required_area = float(request.form['required_area'])
        # amount_layers = int(request.form['amount_layers'])

        # calculations = calc_amount(required_area, amount_layers)
        session_name = new_calculation.session_name
        x = new_calculation.calculate
        print(session_name)
        print(x())
        area = 2
        resin = 3
        hardner = 1
        cost = 2
        # area = new_calculation.calculate["area"]
        # resin = new_calculation.calculate["resin"]
        # hardner = new_calculation.calculate["hardner"]
        # cost = new_calculation.calculate["cost"]

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

    get_default_values = Default_values.query.first()
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

if __name__ == '__main__':
	app.run(debug=True)