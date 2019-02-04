import os,sys,time,random
R = '\033[31m'
Y = '\033[33m'
X = '\033[36m'
bl = '\033[34m'
B = '\033[1m'
W = '\033[00m'
i = ""+R+"["+Y+"+"+R+"]"+W+""
b = "%s[%s-%s]%s" % (R,Y,R,W)
l = "%s[%s!%s]%s" % (R,Y,R,W)
def acakkata(): # list kata
	katakat = open("kata.txt").readlines()
	katakata = ['mutlak',
			'kontol',
			'memek',
			'penis',
			'ngentot',
			'kuygelud',
			'gay',
			'fuckyou',
			'kamu',
			'bangsat',
			'monyet'
			'benar',
			'terserap',
			'sangat',
			'pergi',
			'diapergi',
			'bantu',
			'bantuan',
			'dibantu',
			'pusing',
			'sakit',
			'sakithati',
			'pengen',
			'ane',
			'we',
			'sendiri',
			'jomblo',
			'nyata',
			'ternyata',
			'mempunyai',
			'pasang',
			'pasangan',
			'dinamakan',
			'sayaorgil',
			'menonjolkan',
			'aktivis',
			'sebenarnya',
			'aktualitas',
			'remaja',
			'mempengaruhi',
			'terpengaruh',
			'udara',
			'waspada',
			'sepanjangwaktu',
			'mengalegorisasikan',
			'persekutuan',
			'aliansi',
			'kiasan',
			'sindiran',
			'baik',
			'jahat',
			'sayang',
			'sange',
			'samasekali',
			'memperkuat',
			'analisis',
			'semu',
			'tampaknya',
			'penampilan',
			'menangkap',
			'menilai',
			'penilaian',
			'anggapan',
			'astronomis',
			'sikap',
			'rata-rata',
			'sadar',
			'kesadaran',
			'bayi',
			'padadasarnya',
			'tongkat',
			'kepercayaan',
			'keyakinan',
			'besar',
			'darah',
			'berbasisluas',
			'tanpahenti',
			'pusat',
			'bersertifikat',
			'nyanyian',
			'klaim',
			'rahasia',
			'memikirkan',
			'tanggungjawab',
			'komentar',
			'komentator',
			'lengkap',
			'samasekali',
			'memahami',
			'terpadu',
			'curhat',
			'dugaan',
			'hatinurani',
			'kesadaran',
			'besar',
			'kata',
			'cinta',
			'love',
			'allah',
			'tuhan',
			'dajjal',
			'xxxvideos',
			'porno',
			'dosa',
			'anjing',
			'goblok',
			'ane',
			'www',
			'sangat',
			'katakata',
			'tebakaku',
			'angka',
			'tebakkata',
			'tebakangka',
			'luh',
			'gue',
			'gw',
			'loh',
			'pasangan',
			'jenis',
			'kelamin',
			'jeniskelamin',
			'rumah',
			'kalimat',
			'burung',
			'buruk',
			'alat',
			'virus',
			'kapal',
			'tenggelam',
			'pesawat',
			'alien',
			'laut',
			'bumi',
			'neraka',
			'surga',
			'nerakasurga',
			'vagina',
			'andaikan',
			'master',
			'mastah',
			'noob',
			'newbie',
			'pemula',
			'detik',
			'jam',
			'menit',
			'hari',
			'anak',
			'youandme',
			'kamudansaya',
			'hari',
			'matahari',
			'bimasakti',
			'ailovyu',
			'fakyu',
			'kurus',
			'gendut',
			'gempa',
			'tsunami',
			'asteroid',
			'meteor',
			'teror',
			'manusia',
			'orang',
			'tua',
			'orangtua',
			'tatakrama',
			'sosial',
			'alam',
			'kiamat',
			'semesta',
			'galaksi',
			'extrem',
			'extra',
			'ilysm',
			'skrip',
			'senin',
			'selasa',
			'akhir',
			'terakhir',
			'pertama',
			'kedua',
			'tata',
			'krama',
			'tatakrama',
			'disiplin',
			'kedisiplinan',
			'angkat',
			'itu',
			'dia',
			'gantung',
			'waktu',
			'adalah',
			'uang',
			'pepatah',
			'waktuadalahuang',
			'tepat',
			'tepatwaktu',
			'kapan',
			'dimana',
			'aman',
			'diamankan',
			'tidakaman',
			'pakai',
			'pakaikan',
			'pakaikandia',
			'bunuhdia',
			'tendang',
			'tendangdia',
			'ferguso',
			'mudah',
			'susah',
			'gampang',
			'murah',
			'mahal',
			'kali',
			'sekali',
			'kapanakumati',
			'kapandiamati',
			'coli',
			'coly',
			'colmek',
			'onani',
			'masturbasi',
			'justru',
			'justruitu',
			'rabu',
			'kamis',
			'jumat',
			'sabtu',
			'minggu',
			'tai',
			'api',
			'islam',
			'agama',
			'jokontol',
			'pranjing',
			'kuntilanak',
			'hantu',
			'setan',
			'pocong',
			'valak',
			'ghost',
			'rip',
			'iblis',
			'jembatan',
			'anda',
			'nama',
			'ibu',
			'ayah',
			'kakek',
			'nenek',
			'presiden',
			'raja',
			'aneh',
			'seribu',
			'tangan',
			'manusia',
			'alatkelamin',
			'kamar',
			'mandi',
			'bintang',
			'batal',
			'hakim',
			'keluar',
			'diusir',
			'dikeluarkan',
			'kurang',
			'bencong',
			'bujank',
			'burik',
			'aplikasi',
			'windows',
			'android',
			'oppo',
			'vivo',
			'alienware',
			'telepon',
			'nomor',
			'keyboard',
			'layar',
			'sentuh',
			'pintar',
			'cerdas',
			'bodoh',
			'faedah',
			'berfaedah',
			'unfaedah',
			'akun',
			'pengen',
			'ingin',
			'rindu',
			'cloud',
			'bisa',
			'stres',
			'stroke',
			'kepala',
			'kamus',
			'terjemahan',
			'terjehmakan',
			'ilmu',
			'indonesia',
			'inggris',
			'negara',
			'asean',
			'asia',
			'inti',
			'mars',
			'dalam',
			'doa',
			'berdoa',
			'doakan',
			'tewas',
			'mati',
			'meninggal',
			'dunia',
			'televisi',
			'programmers',
			'python',
			'php',
			'bash',
			'javascript',
			'typescript',
			'ruby',
			'bootstrap',
			'java',
			'objectivec',
			'brainfuck',
			'haskell',
			'dll',
			'bulat',
			'bumidatar',
			'bumibulat',
			'berputar',
			'bunuh',
			'membunuh',
			'isis',
			'teroris',
			'herobrinepeanakanjingkaumgay',
			'qwertyuiopasdfghjklzxcvbnm',
			'oanxoscsxxlakaoxnsocjsowncosnfosnxksnckndkscnskcnskxnalsnwoddk',
			'blablaandbla',
			'lainlain']
	kataterpilih = random.choice(katakata)
	return kataterpilih
def cektebakan(parsekata,huruftebakan=None):
	if huruftebakan in parsekata:
		return True
	else:
		return False
def hitunginput(huruftebakan):
	count = 0
	for i in huruftebakan:
	  	count += 1
	return count
def progresskata(parsekata,progress,huruftebakan=None):
	if progress == None:
		progress = []
		for i in parsekata:
			progress.append('*')
	for i in (i for i,x in enumerate(parsekata) if x == huruftebakan):
		progress[i] = str(huruftebakan)
	return progress
def cekh():
	hadiah = ['kontol',
			'memek',
			'monyet',
			'tai',
			'pisang',
			'daging kontol',
			'bakso tikus',
			'Oppo Find X',
			'Vivo',
			'Alienware',
			'Oppo F9',
			'kata selamat',
			'Iphone X',
			'aipon eks',
			'racun tikus',
			'sampah',
			'botol akulah',
			'narkoba',
			'sabu',
			'satelit',
			'bekicot',
			'alien',
			'CD',
			'BH',
			'celana dalam',
			'otak',
			'pulsa',
			'sate tikus',
			'kopi',
			'susu gantung',
			'toge',
			'payudara',
			'donat',
			'sosis',
			'donat-sosis',
			'pantat',
			'topi',
			'topeng anonytikus',
			'ular',
			'ulargerak',
			'kuota 100 GB',
			'pulsa',
			'memekontol',
			'pantat hitam',
			'lubang hitam',
			'ah',
			'motor',
			'mobil',
			'mm',
			'bla']
	ch = random.choice(hadiah)
	cj = random.choice(hadiah)
	ck = random.choice(hadiah)
	hd = ["""
 {}Hadiah {}> {}{}
          {}
          {}\n""".format(W,R,W,ch,cj,ck),
			"""
 {}Hadiah {}> {}{}
          {}
          {}\n""".format(W,R,W,ch,cj,ck)]
	hdd = random.choice(hd)
	bs = """
{}[{}1{}] {}Lihat Hadiah
{}[{}2{}] {}Lanjut
{}[{}3{}] {}Keluar

 {}[{}?{}] {}>>> {}""".format(R,Y,R,W,R,Y,R,W,R,Y,R,W,R,Y,R,R,W)
	bb = input(bs)
	if bb == '1':
		print("""
 {}Hadiah {}> {}{}
          {}
          {}\n""".format(W,R,W,ch,cj,ck))
		abl = input("Ambil Hadiah ? [y/t] : ")
		if abl == 'y' or abl == 'Y':
			print("\nMaaf, Kamu Tidak Bisa Mengambilnya, karena kamu orang miskin\n")
			pass
		elif abl == 't' or abl == 'T':
			pass
		else:
			print("")
			pass
	elif bb == '2':
		print("")
		main()
	elif bb == '3':
		KeyboardInterrupt
	else:
		cekh()
def tebaklangsung(parsekata,huruftebakan):
	kata = ''.join(parsekata)
	tebak = ''.join(huruftebakan)

	if kata == tebak:
		return True
	else:
		return False
def cekselesai(progress):
	ada = -1
	for i in (i for i,x in enumerate(progress) if x == '*'):
		ada = i
	if ada != -1:
		return True
	else:
		return False
def join(kata):
	kata = ' '.join(kata)
	return kata
def sudahdipilih(baghuruf,pilihan):
	ada = -1
	for i in (i for i,x in enumerate(baghuruf) if x == pilihan):
		ada = i
	if ada != -1:
		return True
	else:
		return False
def klr():
  print("\n\n\n"+i+" Thanks sudah Pake Tuls ai ...")
  print(i+" Semoga Harimu Buruk ! ...\n")
  sys.exit()
y = "\033[33;1m"
P = '\033[37m'
def banner():
	print("                       %s  *  %sTebakKata   %s*" % (R,y,R))
	print("                     %s-----------------------" % (Y))
	print("                       %s   Author : saya" % (P))
	print("                     %s-----------------------" % (Y))
	print("                       %s   Tool   : Hiburan" % (P))
	print("                     %s-----------------------\n" % (Y))

def main():
 try:
	 kata = acakkata()
	 parsekata = list(kata)
	 panjangkata = len(parsekata)
	 progress = None
	 tertebak = False
	 telahdipilih = []
	 langkah = 0
	 while not tertebak:
		 print(""+i+" Kata berisi %d huruf, " % panjangkata, end='')
		 huruftebakan = input("silahkan tebak 1 huruf: ")
		 jmltebakan = hitunginput(huruftebakan)
		 if jmltebakan == 1:
			 cektlhdipilih = sudahdipilih(telahdipilih,huruftebakan)
			 if cektlhdipilih:
				 print(b+' Anda sudah menebak huruf %s sebelumnya.' % huruftebakan)
				 print(join(progress))
				 continue
			 else:
				 telahdipilih.append(huruftebakan)
			 cekada = cektebakan(parsekata,huruftebakan)
			 if cekada:
				 progress = progresskata(parsekata,progress,huruftebakan)
				 print(join(progress))
			 else:
				 print(b+' Tidak mengandung huruf ', huruftebakan)
				 print(join(progress))
			 selesai = cekselesai(progress)
			 if not selesai:
				 print(i+' Selamat kamu berhasil !!!')
				 print(i+" Kata \033[36m""%s"" \033[00mtertebak dalam %d langkah\n" % (join(parsekata),langkah))
				 tertebak = True
				 cekh()
		 else:
			 if jmltebakan == 0:
				 print(b+' Tidak ada input, masukkan satu huruf.')
				 print(join(progress))
			 else:
				 langsung = tebaklangsung(parsekata,huruftebakan)
				 if langsung == True:
					 print(i+' Selamat tebakan langsung anda berhasil!!!')
					 print(i+' Kata ''%s'' tertebak dalam %d langkah.' % (join(parsekata),langkah))
					 tertebak = True
				 else:
					 print(b+' Tebakan langsung anda belum tepat.')
					 print(join(progress))
		 langkah += 1
 except EOFError:
  klr()
 except KeyboardInterrupt:
  klr()
 except:
  main()
if __name__ in "__main__":
 os.system("clear")
 banner()
 main()
