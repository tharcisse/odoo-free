{
    'name': 'Company legal informations',
    'version': '17.0.0.1.0',
    'description': '',
    'summary': 'Company Legal Informations',
    'author': 'Imanis,Tharcisse Mukundayi',
    'website': 'https://github.com/tharcisse',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/company_section.xml',
        'data/company_division.xml',
        'data/company_group.xml',
        'data/company_classification.xml',
        'data/business_model.xml',
        'data/legal_structure.xml',
        'views/document_viewx.xml',
        'views/share_views.xml',
        'views/shareholder_views.xml',
        'views/company_views.xml',
        'views/classification_views.xml',


    ],
    'auto_install': False,
    'application': False,
}