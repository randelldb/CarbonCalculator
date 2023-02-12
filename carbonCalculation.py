class CarbonCalculation:
    def __init__(self, session_name, area, layers, default_values) -> None:
        self.session_name = session_name
        self.area = area
        self.layers = layers
        self.default_values = default_values
    
    def calculate(self):
        get_default_setting     = self.default_values.query.first()
        resin_weight            = get_default_setting.resin_weight
        price_resin             = get_default_setting.price_resin
        hardner_weight          = get_default_setting.hardner_weight
        default_carbon_area     = get_default_setting.default_carbon_size_width * get_default_setting.default_carbon_size_height
        default_carbon_weight   = get_default_setting.default_carbon_weight
        price_carbon            = get_default_setting.price_carbon

        calc_req_area       = (self.area / default_carbon_area) * self.layers
        calc_req_resin      = (calc_req_area * default_carbon_weight) / 100 * 120
        calc_req_hardner    = (calc_req_resin / 2) / 100 * 120
        est_cost = ((calc_req_resin / resin_weight) * price_resin) + ((calc_req_hardner / hardner_weight) * price_resin) + calc_req_area * price_carbon

        result = {
            "area" : str(round(calc_req_area, 3)),
            "resin" : str(round(calc_req_resin, 3)),
            "hardner" : str(round(calc_req_hardner, 3)),
            "cost" : str(round(est_cost, 2)),
        }

        return result