from odoo import models,fields,api,_
from datetime import date
from datetime import datetime

class Depenses(models.Model):
    _name = "liste.depenses"
    _description = ""

    mofit= fields.Char(string="Mofit")
    date_depense=fields.Datetime(string="Du")
    montant = fields.Integer(string="Montant dépanse")
