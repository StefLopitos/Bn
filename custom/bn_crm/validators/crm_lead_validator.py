# -*- coding: utf-8 -*-
import re

from odoo.exceptions import ValidationError


class LeadValidator:
    def __init__(self, lead):
        self._lead = lead
        self._message_validation = ''

    def validate_create(self):
        self.validate_email()
        if self._message_validation != '':
            raise ValidationError(self._message_validation)

    def validate_email(self):
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self._lead.email_from)
        if match is None:
            self._message_validation = 'No es un correo valido'
