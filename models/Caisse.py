from odoo import models,fields,api,_
from datetime import date
from datetime import datetime

class Caisse(models.TransientModel):
    _name = "caisse"
    _description = ""


    date_debut = fields.Datetime(string="Du",default=fields.Date.today())
    date_fin = fields.Datetime(string="A",default=fields.Date.today())
    solde = fields.Integer(string="Solde")
    montant_total_ventes = fields.Integer(string="Montant total des ventes")
    montant_total_remises = fields.Integer(string="Montant total des remises")
    montant_total_depenses = fields.Integer(string="Montant total des dépenses")

    @api.depends("date_debut","date_fin")
    def calculet_global_totale(self):
        liste = self.env['liste.ventes'].search([])
        depenses = self.env['liste.depenses'].search([])
        if self.date_debut  and self.date_fin :
            li = liste.filtered(lambda rec : rec.create_date >= self.date_debut and rec.create_date <= self.date_fin)
            dep = depenses.filtered(lambda rec : rec.date_depense >= self.date_debut and rec.date_depense <= self.date_fin)
        elif self.date_debut and self.date_fin==False:
            li = liste.filtered(lambda rec : rec.create_date >= self.create_date)
            dep = depenses.filtered(lambda rec : rec.date_depense >= self.date_debut)
        elif self.date_debut==False and self.date_fin:
            li = liste.filtered(lambda rec :rec.create_date <= self.date_fin)
            dep = depenses.filtered(lambda rec :rec.date_depense <= self.date_fin)
        else :
            li = liste
            dep = depenses


        ma = li.mapped("global_total")
        remise = li.mapped("net_payer")
        de = dep.mapped("montant")
        print("-----------------",depenses)
        print("-----------------",dep)
        print("-----------------",de)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("++++++++++++++++++++++",li)
        print("<<<<<>>>>>>>>>>>>>>",ma)
        print("<<<<<>>>>>>>>>>>>>>",remise)
        com = 0
        rem=0
        depenses_total = 0
        for rec in de:
            depenses_total = depenses_total+rec
        for rec in ma:
            com = com+rec
        for rec in remise:
            rem = rem+rec
        for rec in self:
            rec.montant_total_ventes = com
            rec.montant_total_remises = rem
            rec.montant_total_depenses = depenses_total
            rec.solde = rec.montant_total_ventes - rec.montant_total_depenses
        print('EEEEEEEE',com)




    def name_get(self):
        for rec in self:
            return [(rec.id,"Date de visionnage d'intérêt : %s"%rec.create_date)]