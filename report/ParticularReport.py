from odoo import api, models

class ParticularReport(models.AbstractModel):
    _name = 'report.resto.report_liste_articles'


    @api.model
    def _get_report_values(self, docids, data=None):
        # get the report action back as we will need its data
        docs = self.env['liste.articles'].search([])
        # get the records selected for this rendering of the report
        print("VVVVVV",docs)
        # return a custom rendering context
        return {
            'docs': docs
        }