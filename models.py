# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Cliente(models.Model):
    _name = 'masaje.cliente'
    name = fields.Char(string="Nombre", required=True)
    
class Empleado(models.Model):
    _name = 'masaje.empleado'
    name = fields.Char(string="Nombre", required=True)
    tipo = fields.Char(string ="Puesto", required=True)
    nacionalidad_id = fields.Many2one('masaje.nacionalidad', string="Nacionalidad")

class Nacionalidad(models.Model):
	_name = 'masaje.nacionalidad'
	name = fields.Char(string="Nombre", required=True)
	empleado_id = fields.One2many('masaje.empleado','nacionalidad_id', string="Empleado")



 

   

