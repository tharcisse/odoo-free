{
    'name': 'Brevo Basic Sync',
    'version': '1.0',
    'description': 'Brevo Basic Sync',
    'summary': """
    Synchronize:
    - Contacts
    - Contact Attributes
    """,
    'author': 'Grevlin,Tharcisse Mukundayi',
    'website': 'https://github.com/tharcisse',
    'license': 'LGPL-3',
    'category': 'Marketing',
    'depends': [
        'base','contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/attributes.xml',
        'data/brevo_cron.xml',
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
        'views/brevo_attributes_views.xml',
        'views/menu.xml'
    ],
    
    'auto_install': False,
    'application': False,
    'external_dependencies':{
        'python':[
            'brevo-python'
        ]
    }
}