# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odootycoon_plus(models.Model):
#     _name = 'odootycoon_plus.odootycoon_plus'
#     _description = 'odootycoon_plus.odootycoon_plus'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
