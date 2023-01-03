
def tambah_aktivitas(nama,tanggal,kategori):
    global jadwal

    if nama.lower() in [nama_k.lower() for nama_k in jadwal]:
        return 'Kegiatan sudah pernah diinput. Tidak boleh double claim!'
    else:
        jadwal[nama] = [tanggal,kategori,jadwal_poin_kegiatan[kategori]]
        return 'Kegiatan berhasil ditambahkan.'



jadwal = {}

jadwal_poin_kegiatan = {
    'Prestasi':30,
    'Organisasi':10,
    'Kepanitiaan':5,
    'Rekognisi':2
}



Tidakmau_keluar = True

while Tidakmau_keluar:
    print('******* Kredit Keaktifan Mahasiswa ******\n(Student Activities Credit)')

    choices = ['Menambahkan Kegiatan', 'Menampilkan Jumlah Poin', 'Keluar']

    for i, choice in enumerate(choices,start=1):
        print(f'{i}. {choice}')

    print('-'*30)

    memilih = choices[int(input('Silahkan Masukan Pilihan Anda: '))-1]

    if memilih == choices[0]:
        nama_aktivitas = input('Nama Kegiatan: ')
        tanggal_aktivitas = input('Tanggal Kegiatan: ')
        print('Pilihan Kategori Kegiatan:')
        for poin in jadwal_poin_kegiatan:
            print(f' - {poin}')
        kategori_kegiatan = input('Masukan Kategori Kegiatan: ').title()
        print('')
        print(tambah_aktivitas(nama_aktivitas,tanggal_aktivitas,kategori_kegiatan))
        print('')
    elif memilih == choices[1]:
        print('')
        print('-'*30,end='')
        print('Nama Kegiatan\tTanggal\tKategori\tPoin')
        jumlah_poin = 0
        for i, jadwal_terdaftar in enumerate(jadwal,start=1):
            print(f'{i}. {jadwal_terdaftar}',end='\t')
            print(*jadwal[jadwal_terdaftar],sep='\t')
            jumlah_poin += jadwal[jadwal_terdaftar][-1]
        print(f'JUMLAH TOTAL POIN\t: {jumlah_poin}')
        print('')
    else:
        print('Sistem Berhenti...')
        belum_keluar = False
