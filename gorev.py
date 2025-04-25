class Ogrenciler:
  def __init__(self):
    self.ogrenciler=[]
    self.mevcut=0
  def ogrenciler_ekle(self,ogrenci):
    self.ogrenciler.append(ogrenci)
  def ogrenciler_goster(self):
    for ogrenci in self.ogrenciler:
      print(ogrenci.isim,ogrenci.numara)
  def sinifa_ogrenci_girsin(self):
      self.mevcut+=1


class ogrenci:
  def __init__(self,isim,numara):
    self.isim=isim
    self.numara=numara
class Ders:
    def __init__(self, ders_ad, ders_kod):
        self.ad = ders_ad
        self.kod = ders_kod

class Dersler:
    def __init__(self):
        self.ders_listesi = []
        self.toplam_ders = 0

    def ders_ekle(self, ders):
        self.ders_listesi.append(ders)
        self.toplam_ders += 1

    def dersleri_goster(self):
        for ders in self.ders_listesi:
            print(ders.ad, ders.kod)