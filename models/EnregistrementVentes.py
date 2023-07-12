from odoo import models,fields,api,_

class EnregistrementVentes(models.Model):
    _name = "enregistrement.ventes"
    _description = ""


    orderlines_id = fields.Many2one('liste.articles', string='Article')
    qte = fields.Integer(string="Qte",default=1)
    total = fields.Integer(string="Total",default=0,compute="calculer_prix")

    @api.depends("qte","orderlines_id")
    def calculer_prix(self):
        for rec in self:
            pr=0
            for record in rec.orderlines_id:
                pr = record.prix
            rec.total = rec.qte * pr
