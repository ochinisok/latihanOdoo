from odoo import api, fields, models


class Kategori(models.Model):
    _name = 'kategori'
    _description = 'Tabel Kategori'

    name = fields.Char(string='Name', Required=True)
    keterangan = fields.Char(string='Keterangan')
    buku_id = fields.Many2many(comodel_name='buku', string='Judul Buku')
    
    

