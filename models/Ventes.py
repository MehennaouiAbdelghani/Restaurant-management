from odoo import models,fields,api,_
from datetime import date
from datetime import datetime

class Ventes(models.Model):
    _name = "liste.ventes"
    _description = ""
    #le compte est :
    #parametre pre difini
    n_vente = fields.Char(string="N° Vente")
    # Vente
    remise = fields.Integer(string="Remise",default=0)
    net_payer = fields.Integer(string="Net à Payer",default=0,compute="calcul_remise")
    #t3awnek ch7al treje3
    versement = fields.Integer(string="Versement",default=0)
    rendu = fields.Integer(string="Rendu",default=0,compute="calcul_remise")
    # des donne de article
    nomarticle_ids = fields.Many2many("enregistrement.ventes",string="Nom Article")
    # pre total
    global_total = fields.Float(string="Total",default=0,compute="calculet_global_totale")



    @api.depends("remise","versement")
    def calcul_remise(self):
        for rec in self:
            if rec.remise:
                rec.net_payer = rec.global_total - rec.remise
            else:
                rec.net_payer = 0
            if rec.versement:
                rec.rendu = (rec.versement - rec.global_total) + rec.net_payer
            else:
                rec.rendu = 0


    @api.depends("nomarticle_ids")
    def calculet_global_totale(self):
        val_liste=[]
        for record in self:
            compte = 0
            if record.nomarticle_ids:
                for rec in record.nomarticle_ids:
                    compte = compte + rec.total
                print("+++++++++++++++++++++")
                print(compte)
                print("+++++++++++++++++++++")
            record.global_total = compte




    @api.model
    def create(self, vals_list):
        vals_list['n_vente'] = self.env['ir.sequence'].next_by_code('ventes.sequence')
        print(">>>>>>",vals_list)
        return super(Ventes , self).create(vals_list)

    def name_get(self):
        for rec in self:
            return [(rec.id,"Le processus de vente qui a compté %s" % rec.n_vente)]