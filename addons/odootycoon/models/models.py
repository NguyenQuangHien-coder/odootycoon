# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError, Warning
from random import randint 
    
class odootycoon_producttemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    unlockcost = fields.Float('Unlock Cost', default=750)
    unlocked = fields.Boolean('Unlocked', default=False)

    # Button: unlockproduct 
    def unlockproduct(self):
        print('Unlock Product')
        gamemanager = self.env['odootycoon.gamemanager'].search([('name', '=', 'New Game')])
        #When your cash >= unlockcost, you can click UnlockButton. And you have to pay the unlockcost to unlock product
        #gamemanager.cash is your money
        #unlockcost is the money you must to pay for unlock the product
        if gamemanager.cash >= self.unlockcost:
            self.unlocked = True
            gamemanager.cash -= self.unlockcost
        else:
            #Must import the library's name is "Warning" before use syntax below
            raise Warning('You do not have enough money to unlock the %s product' % self.name)

class odootycoon_gamemanager(models.Model):
    _name = "odootycoon.gamemanager"
    _description = "My Odoo project"

    name = fields.Char("Game Name", default="New Game")
    day = fields.Integer("Current day", default=1)
    cash = fields.Float("Cash", default=1000)

# Button--------------------------------------------:
    def nextday(self):
        #Process Unlocked Products
        products = self.env['product.template'].search([('unlocked','=', True)])
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

