{
    'name' : 'IT Assets',
    'author' : 'Ahmed Hefny',
    'category' : '',
    'version' :'18.0.0.1.0',
    'depends': ['base', 'mail'],
    'data' : [
        'security/ir.model.access.csv',
        "views/base_menu.xml",
        "views/device_view.xml",
        "views/category_view.xml",
        "views/specs_view.xml",
    ],
    'installable': True,
    'application' : True,
    'license': 'LGPL-3',
}