
JADWAL = {}

jadwal_poin_kegiatan = {
    'Prestasi':30,
    'Organisasi':10,
    'Kepanitiaan':5,
    'Rekognisi':2
}



tidakbisa_keluar = True

while tidakbisa_keluar:
    print('******* Kredit Keaktifan Mahasiswa ******\n(Student Activities Credit)')

    choices = ['Menambahkan Kegiatan', 'Menampilkan Jumlah Poin', 'Keluar']

    for i, choice in enumerate(choices,start=1):
        print(f'{i}. {choice}')

    print('-'*30)

    list = choices[int(input('Silahkan Masukan Pilihan Anda: '))-1]

    if list == choices[0]:
        nama_aktivitas = input('Nama Kegiatan: ')
        tanggal_aktivitas = input('Tanggal Kegiatan: ')
        print('Pilihan Kategori Kegiatan:')
        for poin in jadwal_poin_kegiatan:
            print(f' - {poin}')
        kategori_event = input('Masukan Kategori Kegiatan: ').title()
        print('')
        print(tambah_aktivitas(nama_aktivitas,tanggal_aktivitas,kategori_event))
        print('')
    elif list == choices[1]:
        print('')
        print('-'*30,end='')
        print('Nama Kegiatan\tTanggal\tKategori\tPoin')
        total_nilai = 0
        for i, kegiatan_terdaftar in enumerate(JADWAL,start=1):
            print(f'{i}. {kegiatan_terdaftar}',end='\t')
            print(*JADWAL[kegiatan_terdaftar],sep='\t')
            total_nilai += JADWAL[kegiatan_terdaftar][-1]
        print(f'JUMLAH TOTAL POIN\t: {total_nilai}')
        print('')
    else:
        print('Sistem Berhenti...')
        tidakbisa_keluar = False