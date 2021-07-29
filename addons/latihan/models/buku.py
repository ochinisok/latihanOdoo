from odoo import api, fields, models


class Buku(models.Model):
    _name = 'buku'
    _description = 'Tabel Buku'

    name = fields.Char(string='Judul Buku', Required=True)
    isbn = fields.Char(string='ISBN')
    jumlah = fields.Integer(string='Jumlah Buku')
    keterangan = fields.Text(string='Keterangan Buku')
    pengarang_id = fields.Many2one(comodel_name='pengarang', string='Nama Pengarang')
    kategori_id = fields.Many2many(comodel_name='kategori', string='Kategori Buku')
    
    
