# Kinanthi (71210745)
# UG05

class Karyawan:
    _nama = ""
    _umur = 0
    _jenisKelamin = None
    _upahPerHari = None

    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur

    def setNama(self, nama):
        self._nama = nama
    def setUmur(self, umur):
        self._umur = umur
    def setJenisKelamin(self, jenisKelamin):
        self._jenisKelamin = jenisKelamin
    def setUpahPerHari(self, upahHarian):
        self._upahPerHari = upahHarian


    def getNama(self):
        return self._nama
    def getUmur(self):
        return self._umur
    def getJenisKelamin(self):
        return self._jenisKelamin
    def getUpahPerHari(self):
        return self._upahPerHari

    def printInfo(self):
        print("============INFO============")
        print("Nama\t\t:", self.getNama())
        print("Umur\t\t:", self.getUmur())
        print("Jenis Kelamin\t:", self.getJenisKelamin())
        print("Upah per Hari\t:", self.getUpahPerHari())

    def hitungGajiBulanan(self, hari):
        if hari != 30:
            print("ERROR! Upah per Hari belum di inputkan")
        else:
            print("Gaji Bulan ini :", hari * self.getUpahPerHari())

# test case
if __name__ == "__main__":
    orang1 = Karyawan("Haniif", 90)
    orang1.printInfo()

    orang2 = Karyawan("Sindu", 190)
    orang2.setJenisKelamin("Laki-laki")
    orang2.setUpahPerHari(30000)
    orang2.printInfo()

    orang1.hitungGajiBulanan(28)
    orang2.hitungGajiBulanan(30)
