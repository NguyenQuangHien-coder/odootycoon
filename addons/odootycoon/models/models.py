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
    # TEST
    # def test(seft):
    #     raise Warning('test ok')
    # sale_description = fields.Char(string="Sale_Description")
    # /TEST
# TEST
# class Sale__Order(models.Model):
#     __name = 'sale.order'
#     _inherit = 'sale.order'
#     sale_description = fields.Char(string="Sale_Description")
# /TEST

class odootycoon_gamemanager(models.Model):
    _name = "odootycoon.gamemanager"
    _inherits = {'product.template': 'my_product_id'}
    _description = "My Odoo project"

    my_product_id = fields.Many2one(
        'product.template', 'My Product',
        auto_join=True, index=True, ondelete="cascade", required=True)
    # unlocked = fields.Boolean(default=False)

    name = fields.Char("Game Name", default="New Game")
    day = fields.Integer("Current day", default=1)
    cash = fields.Float("Cash", default=1000)
    income = fields.Float("Your Income", default=0)

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
        self.write({'day': self.day + 1, 'cash': self.cash + cash, 'income': self.income + cash})
    def skip5days(self):
        for i in range(0,5):
            self.nextday()
    def skip30days(self):
        for i in range(0,30):
            self.nextday()
    def resetgame(self):
        self.day = 1
        self.cash = 1000
        self.income = 0
        products = self.env['product.template'].search([('unlocked','=',True)]).write({'unlocked':False})
    def unlockproduct(self):
        odoo_product = self.env['product.template'].search([('name', '=', 'Product')])
        if self.cash >= odoo_product.unlockcost:
            products = self.env['product.template'].search([('unlocked','=',False)]).write({'unlocked':True})
            self.cash -= odoo_product.unlockcost
        else:
            raise Warning('Not Enough Money')

class odootycoon_productmanager(models.Model):
    _name = "odootycoon.productmanager"
    _inherits = {'product.template': 'my_product_id'}
    _description = "My Odoo Product Manager"
    
    my_product_id = fields.Many2one(
        'product.template', 'My Product',
        auto_join=True, index=True, ondelete="cascade", required=True)

# class odootycoon_unlockcost(models.Model):
#     _name = "odootycoon.unlockcostmanager"
#     _description = "My Odoo UnlockCost Manager"

#     unlockcost = fields.Float('Unlock Cost', default=750)
        

    
    

       


