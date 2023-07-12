from odoo import models,fields,api,_
from datetime import date
from datetime import datetime

class StatistiqueVents (models.TransientModel):
    _name = "statistique"
    _description = ""



    date_debut = fields.Datetime(string="Du",default=fields.Date.today())
    date_fin = fields.Datetime(string="A",default=fields.Date.today())
    user_id = fields.Many2one("res.users", string="Utilisateur", default=lambda self: self.env.user)
    nomarticles_id=fields.Many2one("liste.articles",default="Tous les Articles",string="Nom Article")
    qte_vendue=fields.Integer(string="Qte")
    qte_totale_chaque_produit=fields.Integer(string="Qte totale chaque produit")
    total=fields.Float(string="totale")
    totale_chaque_produit=fields.Float(string="totale chaque produit")
    porsontage=fields.Float(string="Porsontage")


    @api.depends("nomarticles_id")
    def statistique_vents(self):
        liste = self.env['liste.ventes'].search([])
        print(liste)
        print('***********************************************************************************')
        qte = 0
        total = 0
        qte_totale_chaque_produit = 0
        totale_chaque_produit = 0
        #############################################################
        if self.date_debut  and self.date_fin :
            li = liste.filtered(lambda rec : rec.create_date >= self.date_debut and rec.create_date <= self.date_fin)
        elif self.date_debut and self.date_fin==False:
            li = liste.filtered(lambda rec : rec.create_date >= self.date_debut)
        elif self.date_debut==False and self.date_fin:
            li = liste.filtered(lambda rec :rec.create_date <= self.date_fin)
        else :
            li = liste
            print("liste filtri par date ",li)
        #############################################################
        for rec in li:
            for pordut in rec.nomarticle_ids:
                # claculer         qte_totale_chaque_produit        totale_chaque_produit
                if self.nomarticles_id.name == pordut.orderlines_id.name:
                    print("______________________________________")
                    qte_totale_chaque_produit += pordut.qte
                    totale_chaque_produit += pordut.total
                    print("Article", pordut.orderlines_id.name, "QTE", pordut.qte, "TOTAL", pordut.total)
                    print("______________________________________")
                    if self.user_id.name == pordut.create_uid.name:
                        print("______________________________________")
                        qte += pordut.qte
                        total += pordut.total
                        print("Article", pordut.orderlines_id.name, "QTE", pordut.qte, "TOTAL", pordut.total)
                        print("______________________________________")
                    elif self.user_id.name == False:
                        print("______________________________________")
                        qte += pordut.qte
                        total += pordut.total
                        print("Article", pordut.orderlines_id.name, "QTE", pordut.qte, "TOTAL", pordut.total)
                        print("______________________________________")
                        ############################################################"
                elif self.nomarticles_id.name == False:
                    if self.user_id.name == pordut.create_uid.name:
                        print("______________________________________")
                        qte += pordut.qte
                        total += pordut.total
                        print("Article", pordut.orderlines_id.name, "QTE", pordut.qte, "TOTAL", pordut.total)
                        print("______________________________________")
                    elif self.user_id.name == False:
                        print("______________________________________")
                        qte += pordut.qte
                        total += pordut.total
                        print("Article", pordut.orderlines_id.name, "QTE", pordut.qte, "TOTAL", pordut.total)
                        print("______________________________________")
                    qte_totale_chaque_produit += pordut.qte
                    totale_chaque_produit += pordut.total






        print("################################################")
        print(self.nomarticles_id.name)
        print(self.nomarticles_id.name,"QTE TOTOA PRODUITE",qte,"TOTAL",total)
        print(qte_totale_chaque_produit,"|",totale_chaque_produit)
        print("#################################################")
        self.qte_vendue = qte
        self.total = total
        self.qte_totale_chaque_produit=qte_totale_chaque_produit
        self.totale_chaque_produit=totale_chaque_produit
        if qte_totale_chaque_produit != 0:
            self.porsontage = (qte*100)/qte_totale_chaque_produit
        else:
            self.porsontage = 0





