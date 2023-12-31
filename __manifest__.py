{
    "name": "Gestion Restaurant",
    "author": "mehennaoui abdelghani",
    "summary": """Gestion Restaurant""",
    'sequence': 1,
    'version': '1.0.0',
    'category': 'Accounting/Accounting',
    'depends': ['base', 'portal', 'mail', 'utm'],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "report/bon_papier.xml",
        "report/BonVente.xml",
        "report/report.xml",
        "views/Statistique.xml",
        "views/Depenses.xml",
        "views/Caisse.xml",
        "views/EnregistrementVentes.xml",
        "views/Ventes.xml",
        "views/Articles.xml",
        "views/Categories.xml",
        "views/MenuPrincipale.xml",
    ],
    'images': ['static/description/icon.PNG'],
    'css': ['static/src/css/style.css'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
