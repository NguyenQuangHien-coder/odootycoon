# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError, Warning
from random import randint 

class odootycoon_gamemanager(models.Model):
    _name = "odootycoon.gamemanager"
    _description = "My Odoo project"

    name = fields.Char("Game Name", default="New Game")
    day = fields.Integer("Current day", default=1)
    cash = fields.Float("Cash", default=1000)

# Button: Next day
    def nextday(self):
        #Process Unlocked Products
        products = self.env['product.template'].search([('unlocked','=',True)])
        cash = 0
        for product in products:
            #list_price is the Sale Price of each product
            #Must import the library's name is "random" before use syntax below
            numsold = randint(5,35)
            cash += product.list_price *numsold
        self.write({'day': self.day + 1, 'cash': self.cash + cash})
    def skip5days(self):
        for i in range(0,5):
            self.nextday()
    def skip30days(self):
        for i in range(0,30):
            self.nextday()
    def resetgame(self):
        self.day = 1
        self.cash = 1000
        products = self.env['product.template'].search([('unlocked','=',True)]).write({'unlocked':False})

