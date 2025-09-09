{
    'name': 'WhatsApp Float Button',
    'version': '18.0.1.0.0',
    'summary': 'Boton flotante de WhatsApp en todo el sitio web',
    'description': 'Agrega un boton flotante de WhatsApp en la esquina inferior derecha en todo el sitio web.',
    'category': 'Website',
    'author': 'Francisco Toro',
    'website': 'https://your-website-or-github-link.com',
    'license': 'LGPL-3',
    'price': 19.0,
    'currency': 'USD',
    'depends': ['website'],
    'data': [
        'views/res_config_settings_view.xml',
        'views/whatsapp_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'whatsapp_float_button/static/src/css/whatsapp.css',
        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
        'static/description/screenshot.png',
        'static/description/screenshot2.png',
        'static/description/thumbnail.png',
        'static/description/banner2.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
