from odoo import models,fields,api,_
class Article(models.Model):
    _name = "liste.articles"
    _description = ""
    _rec_name = "name"

    name = fields.Char(string="Nom")
    prix = fields.Float(string="Le prix du plat")
    photo = fields.Image(string="Photo")
    categorue_id =fields.Many2one("gestion.categories",string="Catégorie")






