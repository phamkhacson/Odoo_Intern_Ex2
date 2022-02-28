{
    'name': 'Product Warranty',
    'version': '1.3',
    'sequence': 10,
    'description': """ """,
    'category': 'Products',
    'license': 'LGPL-3',
    'depends': ['sale', 'contacts'],
    'data': [
        'views/product_warranty.xml',
        'views/warranty_on_cart_template.xml',
        'security/group.xml'
    ],
    'demo': [
    ],
    'qweb': [],
    'installable': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
