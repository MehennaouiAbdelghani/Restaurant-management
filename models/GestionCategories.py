from odoo import models,fields,api,_

class GestionCategories(models.Model):
    _name = "gestion.categories"
    _description = ""
    _rec_name = "nom_categorie"


    nom_categorie = fields.Char(string="Catégorie",required=True)