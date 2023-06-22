{
    'name': "Inbox Notifications and Emails",

    'summary': """
Notifications to both the Odoo Inbox and Email""",

    'description': """
By default, Odoo provides two options for Notification Management:

* Handle by Emails: notifications are sent to the users' email. This is the default option for new user creation
* Handle in Odoo: notifications appear in the users' Odoo Inbox but no email sent to the users

This module does the following
------------------------------

**Handle by Emails** now offers both inbox and email notifications
    """,

    'author': "T.V.T Marine Automation (aka TVTMA),Viindoo",
    'website': 'https://viindoo.com',
    'live_test_url': 'https://v12demo-int.erponline.vn',
    'support': 'apps.support@viindoo.com',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Discuss',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    'installable': True,
    'application': False,
    'auto_install': True,
    'price': 18.9,
    'currency': 'EUR',
}
