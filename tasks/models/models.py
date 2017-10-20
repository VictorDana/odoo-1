# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tasks(models.Model):
     _name = 'tasks.tasks'

     name = fields.Char()
     start_date = fields.Datetime()
     done = fields.Boolean()
