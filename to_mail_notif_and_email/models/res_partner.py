# -*- coding: utf-8 -*-
from odoo import models, api

class Partner(models.Model):
    _inherit = 'res.partner'
    
    @api.model
    def _notify(self, message, rdata, record, force_send=False, send_after_commit=True, model_description=False, mail_auto_delete=True):
        res = super(Partner, self)._notify(message, rdata, record, force_send, send_after_commit, model_description, mail_auto_delete)
        notifications = self.env['mail.notification'].sudo().search([('mail_message_id', '=', message.id)])
        if notifications:
            notifications.write({            
                'is_read': False,            
            })                
        return res

