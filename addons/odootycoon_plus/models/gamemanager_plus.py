# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError, Warning
from random import randint 
    
class gamemanager_plus(models.Model):
    _name = 'gamemanager.plus'
    _inherit = 'odootycoon.gamemanager'