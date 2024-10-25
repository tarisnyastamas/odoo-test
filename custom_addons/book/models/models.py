# -*- coding: utf-8 -*-

from odoo import models, fields


class Book(models.Model):
    _name = 'book.book'
    _description = 'Model for book'

    name = fields.Char()
    author_ids = fields.Many2many('book.author', string='Authors')
    no_of_pages = fields.Integer()
    genre = fields.Char()


class Author(models.Model):
    _name = 'book.author'
    _description = 'Model for author'

    name = fields.Char()

