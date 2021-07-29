from odoo import api, fields, models


class Pengarang(models.Model):
    _name = 'pengarang'
    _description = 'Tabel Pengarang'

    name = fields.Char(string='Nama Pengarang', Required=True)
    jenis_klm = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki-laki'), ('p', 'Perempuan')], default='l')
    tgl_lahir = fields.Date(string='Tgl Lahir')
    tmpt_lahir = fields.Text(string='Tempat Lahir')
    
    
    
    
