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

# User input section
name_calculation = input("Name this session: ")
required_area = float(input("What is the needed area in m2: "))
amount_layers = int(input("How many layers is needed: "))

print("########################################")

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
        "cost" : str(round(est_cost, 3))
    }

    return result


calculation = calc_amount(required_area, amount_layers)

# Result print
print("The amount of carbon: " + calculation["area"] + " m2")
print("The amount of resin: " + calculation["resin"] + " grams")
print("The amount of hardner: " + calculation["hardner"] + " grams")
print("Estimated cost: " + calculation["cost"])

print("End of program")