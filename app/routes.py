from flask import render_template,request, Blueprint, redirect

from .extensions import db
from .views.index import CarbonCalculation, insert_session_data, get_session_data
from .models import DefaultValues, CarbonSession

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/index", methods=['POST', 'GET'])
def index():
	
    if request.method == 'POST':
        print('posted')
        new_calculation = CarbonCalculation(str(request.form['session_name']), float(request.form['required_area']), int(request.form['amount_layers']), DefaultValues)

        get_result = new_calculation.calculate
        session_name = get_result()['session_name']
        layers = get_result()['layers']
        area = get_result()['area']
        resin = get_result()['resin']
        hardner = get_result()['hardner']
        cost = get_result()['cost']
        
        insert_session_data(session_name, area, layers, resin, hardner)
        session_data = get_session_data()


        return render_template("index.html", session_name=session_name, area=area, resin=resin, hardner=hardner, cost=cost, session_data = session_data)
    else:
        session_data = get_session_data()
        return render_template("index.html", session_data = session_data)
    
@main.route("/defaults", methods=['POST', 'GET'])
def defaults():
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