import os

#Ücgen şekli için oluşturulan class
class Ucgen:
    def __init__(self,kenarlar,aci,aci1,aci2):
        self.kenarlar = kenarlar
        self.aci = aci
        self.aci1 = aci1
        self.aci2 = aci2


    #Üçgenin kenarlarının kullanıcıdan alındığı metod
    def kenar_input(self):
        for i in range(3):
                while self.kenarlar[i] <= 0:
                    try:
                        self.kenarlar[i] = float(input(f"{i+1}.Kenarin Uzunlugunu Giriniz:"))
                    except ValueError:
                        print("Gecersiz")
                    os.system('cls' if os.name=='nt' else 'clear')

    #Üçgenin açılarının kullanıcıdan alındığı metod
    def aci_input(self):
        while self.aci <= 0:
                try:
                    self.aci = float(input("1.Dar Aci Degerini Giriniz:"))
                except ValueError:
                    print("Gecersiz!")
                os.system('cls' if os.name=='nt' else 'clear')
        while self.aci1 <= 0:
                try:
                    self.aci1 = float(input("2.Dar Aci Degerini Giriniz:"))
                except ValueError:
                    print("Gecersiz!")
                os.system('cls' if os.name=='nt' else 'clear')
        while self.aci2 <= 0:
                try:
                    self.aci2 = float(input("3.Dar Aci Degerini Giriniz:"))
                except ValueError:
                    print("Gecersiz!")
                os.system('cls' if os.name=='nt' else 'clear')


    #Üçgenin olunabilirliği hakkında kenar koşullarının kontrol edildiği metod
    def kenar_kontrol(self):
        flag = 1
        i = 0
        while i < 3 and flag:
            toplam = 0                      #2 kenarın toplamının diğer kenardan büyük olduğunu kontrol edecek değişken
            fark = 0                            #2 kenarın farkının diğer kenardan küçük olduğunu kontrol eden değişken
            kontrol = True
            for j in range(3):
                if j != i:
                    toplam += self.kenarlar[j]
                    if kontrol:
                        fark += self.kenarlar[j]
                        kontrol = False
                    else:
                        fark -= self.kenarlar[j]
                        kontrol = True
            
            #Üçgen olunabilirliğini kontrol eden koşul
            if toplam <= self.kenarlar[i] or abs(fark) >= self.kenarlar[i]:
                flag = 0

            i += 1
        
        if flag == 1:
            print("Verdiginiz Kenar Uzunluklarina Sahip Ucgen Cizilebilir!\n")
        else:
            print("Verdiginiz Kenar Uzunluklarina Sahip Ucgen Cizilemez!\n")


    #Üçgende açı kontrolü ile üçgen olup olmadığına bakan metod
    def aci_kontrol(self):

        if self.aci + self.aci1 + self.aci2 != 180:
            print("Verdiginiz Aci Uzunluguna Sahip Ucgen Cizilemez!\n")
        else:
            print("Verdiginiz Kenar Uzunluklarina Sahip Ucgen Cizilebilir!\n")



#Dış Bükey dörtgen için oluşturulan class
class Dortgen:
    def __init__(self,kenarlar,aci,aci1,aci2,aci3):
        self.kenarlar = kenarlar
        self.aci = aci
        self.aci1 = aci1
        self.aci2 = aci2
        self.aci3 = aci3


    #Dörtgenin kenarlarının kullanıcıdan alındığı metod
    def kenar_input(self):
        for i in range(4):
            while self.kenarlar[i] <= 0:
                try:
                    self.kenarlar[i] = float(input(f"{i+1}.Kenarin Uzunlugunu Giriniz:"))
                except ValueError:
                    print("Gecersiz")
                os.system('cls' if os.name=='nt' else 'clear')


    #Dörtgenin açılarının kullanıcıdan alındığı metod
    def aci_input(self):
        while self.aci <= 0:
            try:
                self.aci = float(input("1.Dar Aci Degerini Giriniz:"))
            except ValueError:
                print("Gecersiz!")
            os.system('cls' if os.name=='nt' else 'clear')

        while self.aci1 <= 0:
            try:
                self.aci1 = float(input("2.Dar Aci Degerini Giriniz:"))
            except ValueError:
                print("Gecersiz!")
            os.system('cls' if os.name=='nt' else 'clear')

        while self.aci2 <= 0:
            try:
                self.aci2 = float(input("3.Dar Aci Degerini Giriniz:"))
            except ValueError:
                print("Gecersiz!")
            os.system('cls' if os.name=='nt' else 'clear')

        while self.aci3 <= 0:
            try:
                self.aci3 = float(input("4.Dar Aci Degerini Giriniz:"))
            except ValueError:
                print("Gecersiz!")
            os.system('cls' if os.name=='nt' else 'clear')


    #Dörtgenin kenar kontrollerinin yapıldığı metod
    def kenar_kontrol(self):
        flag = 1
        i = 0
        while i < 4 and flag:
            toplam = 0
            for j in range(4):
                if j != i:
                    toplam += self.kenarlar[j]
            if toplam <= self.kenarlar[i]:
                flag = 0
            i += 1
        
        if flag == 1:
            print("Verdiginiz Kenar Uzunluklarina Sahip Dis Bukey Dortgen Cizilebilir!\n")
        else:
            print("Verdiginiz Kenar Uzunluklarina Sahip Dis Bukey Dortgen Cizilemez!\n")

    
    #Dörtgenin açılarının kontrol edildiği metod
    def aci_kontrol(self):
        if self.aci + self.aci1 + self.aci2 + self.aci3 != 360:
            print("Verdiginiz Aci Uzunluguna Sahip Dis Bukey Dortgen Cizilemez!\n")
        else:
            print("Verdiginiz Kenar Uzunluklarina Sahip Dis Bukey Dortgen Cizilebilir!\n")


            


choice_menu = 4
while choice_menu != 3:                                                             #MENU DONGUSU

    while choice_menu <= 0 or choice_menu > 3:                                        #YANLIŞ İNPUT İÇİN DÖNEN DÖNGÜ
        try:
            choice_menu = int(input("1-Ucgen\n2-Dis Bukey Dortgen\n3-Cikis\nChoice:"))
        
        except ValueError:
            print("Gecersiz!")

        os.system('cls' if os.name=='nt' else 'clear')

        
    if choice_menu != 3:
        os.system('cls' if os.name=='nt' else 'clear')
        if choice_menu == 1:                                                                #Üçgen seçilirse girilen koşul

            ucgen = Ucgen([0,0,0],0,0,0)

            choice_sekil = 3
            while choice_sekil != 1 and choice_sekil != 2:                                  #YANLIŞ İNPUT İÇİN DÖNEN DÖNGÜ
                try:
                    choice_sekil = int(input("Kenar Uzunluklarini Girmek Icin 1\nDar Aci Degerini Girmek Icin 2 Basiniz!\n"))
                except ValueError:
                    print("Gecersiz!")
                os.system('cls' if os.name=='nt' else 'clear')

            if choice_sekil == 1:                                                           #Kenar kontrol seçilirse girilen koşul
                os.system('cls' if os.name=='nt' else 'clear')

                ucgen.kenar_input()
                ucgen.kenar_kontrol()
                choice_menu = 4
            else:                                                                           #Açı kontrol seçilirse girilen koşul
                os.system('cls' if os.name=='nt' else 'clear')
                
                ucgen.aci_input()
                ucgen.aci_kontrol()
                choice_menu = 4

        else:                                                                               #Dörtgen seçilirse girilen koşul
            
            dortgen = Dortgen([0,0,0,0],0,0,0,0)

            choice_sekil = 3
            while choice_sekil != 1 and choice_sekil != 2:                                  #YANLIŞ İNPUT İÇİN DÖNEN DÖNGÜ
                try:
                    choice_sekil = int(input("Kenar Uzunluklarini Girmek Icin 1\nDar Aci Degerini Girmek Icin 2 Basiniz!\n"))
                except ValueError:
                    print("Gecersiz!")
                os.system('cls' if os.name=='nt' else 'clear')

            if choice_sekil == 1:                                                            #Kenar kontrol seçilirse girilen koşul
                os.system('cls' if os.name=='nt' else 'clear')

                dortgen.kenar_input()
                dortgen.kenar_kontrol()
                choice_menu = 4
            else:                                                                            #Açı kontrol seçilirse girilen koşul
                os.system('cls' if os.name=='nt' else 'clear')
                
                dortgen.aci_input()
                dortgen.aci_kontrol()
                choice_menu = 4

    
    else:
        choice_menu = 3
            
