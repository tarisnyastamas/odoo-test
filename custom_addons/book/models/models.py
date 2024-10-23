# -*- coding: utf-8 -*-

from odoo import models, fields


class Book(models.Model):
    _name = 'book.book'
    _description = 'Model for book'

    name = fields.Char()
    author = fields.Char()
    no_of_pages = fields.Integer()
    genre = fields.Char()

