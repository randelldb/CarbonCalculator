from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Settings
resin_type = "Resin type x"
resin_weight = 1500 #grams
price_resin = 30
hardner_type = "Hardner type x"
price_hardner = 0
hardner_weight = 500 #grams
resin_ratio = 2
hardner_ratio = 1
extra_resin_percent = 20 #%

carbon_type = "3k"
default_carbon_size_width = 1 #m
default_carbon_size_height = 1 #m
default_carbon_area = default_carbon_size_width * default_carbon_size_height #m2
default_carbon_weight = 200 #grams
price_carbon = 43

# Calculation
def calc_amount(required_area, amount_layers):
    calc_req_area = (required_area / default_carbon_area) * amount_layers
    calc_req_resin = (calc_req_area * default_carbon_weight) / 100 * 120
    calc_req_hardner = (calc_req_resin / 2) / 100 * 120
    est_cost = ((calc_req_resin / resin_weight) * price_resin) + ((calc_req_hardner / hardner_weight) * price_resin) + calc_req_area * price_carbon

    result = {
        "area" : str(round(calc_req_area, 3)),
        "resin" : str(round(calc_req_resin, 3)),
        "hardner" : str(round(calc_req_hardner, 3)),
        "cost" : str(round(est_cost, 2))
    }

    return result

@app.route("/")
@app.route("/index", methods=['POST', 'GET'])
def index():
	
    if request.method == 'POST':
        print('x')
        required_area = float(request.form['required_area'])
        amount_layers = int(request.form['amount_layers'])

        calculations = calc_amount(required_area, amount_layers)
        
        area    = calculations["area"]
        resin   = calculations["resin"]
        hardner = calculations["hardner"]
        cost    = calculations["cost"]

        return render_template("index.html", area=area, resin=resin, hardner=hardner, cost=cost)
    else:
        return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)