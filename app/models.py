from .extensions import db

class DefaultValues(db.Model):
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


class CarbonSession(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    session_name    = db.Column(db.String(200), nullable=False)
    area            = db.Column(db.Integer, nullable=False)
    layers          = db.Column(db.Integer, nullable=False)
    amount_resin    = db.Column(db.Float)
    amount_hardner  = db.Column(db.Float)