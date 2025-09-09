{
    'name': 'WhatsApp Float Button',
    'version': '18.0.1',
    'summary': 'Botón flotante de WhatsApp en todo el sitio web',
    'description': 'Agrega un botón flotante de WhatsApp en la esquina inferior derecha en todo el sitio web.',
    'category': 'Website',
    'author': 'Francisco Toro',
    'email': 'ftc.odoo.test@gmail.com',
    'license': 'LGPL-3',
    'price': 19.0,
    'currency': 'USD',
    'depends': ['base', 'website'],
    "data": [
        "views/res_config_settings_view.xml",
        "views/whatsapp_template.xml",
    ],
    'assets': {
        'web.assets_frontend': [
            'whatsapp_float_button/static/src/css/whatsapp.css',
        ],
    },
    'images': [
    	'static/images/banner.png',
        'static/description/icon.png',
        'static/description/screenshot.png',
        'static/description/screenshot2.png',
        'static/description/thumbnail.png',
        'static/description/banner2.png',
    ].
    'installable': True,
    'application': False,
    'auto_install': False,
}
