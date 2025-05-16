# -*- coding: utf-8 -*-
{
    'name': "Product Specification",

    'summary': "Product Specification Module",

    'description': """
    This module allows you to manage product specifications in Odoo.
    You can define specifications for product categories and individual products.
    Each specification can have a unit of measure and a sequence for ordering.
    The module also provides a way to automatically create specifications for products
    based on their category or template.
    Features:
    - Define product specifications
    - Assign specifications to product categories
    - Assign specifications to individual products
    - Automatically create specifications for products based on their category or template
    - Manage specifications in a user-friendly interface
    - View specifications in product forms and lists
    - Filter and search products by specifications
    - Customize the display of specifications in product views
    - Support for multiple units of measure
    - Easy integration with existing Odoo modules
    """,

    'author': "Grevlin,Tharcisse Mukundayi",
    'website': "https://www.grevlin.com",

    
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_category_views.xml',
        'views/product_product_views.xml',
        'views/product_template_views.xml',
        'views/product_specification_views.xml',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

