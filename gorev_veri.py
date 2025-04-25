ogr1 = ogrenci('boran', 42)
ogr2 = ogrenci('arda',76)
ogr3 = ogrenci('ayberk',16)

atikler = Ogrenciler()

atikler.ogrenciler_ekle(ogr1)
atikler.ogrenciler_ekle(ogr2)

atikler.ogrenciler_goster()

for i in range(80):
  atikler.sinifa_ogrenci_girsin()
