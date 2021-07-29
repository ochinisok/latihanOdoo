# latihanOdoo
latihan Odoo

Odoo steps:
1. Install docker
2. Install WSL jika di windows
3. Copas file CEP_Docker.zip ke direktori yang diinginkan lalu extract
4. Open folder di vscode
5. Edit file docker-compose.yml (ubah port jika bentrok, contoh "8069:8069")
6. Via terminal di lokasi file extract tadi: docker exec cep_docker_web_1 /usr/bin/odoo scaffold latihan /mnt/extra-addons
7. Selesai untuk bahan awal
8. Lanjutkan dengan pembuatan file di model, view, daftarkan modul di init model dan init addons/latihan

Terima kasih
