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

name_calculation = input("Name this session: ")
required_area = float(input("What is the needed area in m2: "))
amount_layers = int(input("How many layers is needed: "))

print("########################################")

print("Name of session: " + str(name_calculation))
print("Area of part: " + str(required_area))
print("Amount of layers: " + str(amount_layers))

print("########################################")

calc_req_area = (required_area / default_carbon_area) * amount_layers
calc_req_resin = (calc_req_area * default_carbon_weight) / 100 * 120
calc_req_hardner = (calc_req_resin / 2) / 100 * 120

print("The amount of carbon: " + str(calc_req_area) + " m2")
print("The amount of resin: " + str(calc_req_resin) + " grams")
print("The amount of hardner: " + str(calc_req_hardner) + " grams")

print("End of program")

