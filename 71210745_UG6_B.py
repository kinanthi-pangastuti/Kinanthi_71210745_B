# UG6
# Kinanthi (71210745)

class NodeMahasiswa:

    def __init__(self, nama, ipk, n=None, p=None):
        self._element = nama
        self._ipk = ipk
        self._next = n
        self._prev = p
        
    def getNama(self):
        return self._element
    
    def getIpk(self):
        return self._ipk
    
    def setNama(self,nama):
        self._element = nama
        
    def setIpk(self,ipk):
        self._ipk = ipk


class DoubleLList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def __len__():
        return self.size

    def addElementTail(self, nama, ipk):
        baru = NodeMahasiswa(nama, ipk)

        if (self.size == 0):
            self.head = baru
            self.tail = baru
        else:
            baru.p = self.tail
            self.tail.next = baru
            self.tail = baru
            
        print("data masuk ke tail")
        self.size = self.size + 1

    def deleteLast(self):

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            hapus = self.tail
            self.tail = self.tail.prev
            
            hapus.prev = None
            self.tail.next = None
            
            del hapus

        print("# Data", nama,"terhapus #")
        self.size = self.size - 1

    def printDescending(self):
        print("===== Print Descending =====")

        bantu = self.tail
        
        while bantu != None:
            print("============================")
            print("Nama:\t", bantu.getNama())
            print("IPK:", bantu.getIpk())

            bantu = bantu.prev

    def rataIpk(self):
        pass


# TESTCASE
DLLNC = DoubleLList()

DLLNC.addElementTail('Shalom', 3.9)
DLLNC.addElementTail('Nabilla', 3.8)
DLLNC.addElementTail('Kurniadi', 3.7)
DLLNC.addElementTail('Harris', 3.6)
DLLNC.printDescending()

DLLNC.deleteLast()
DLLNC.printDescending()

#DLLNC.rataIpk()
