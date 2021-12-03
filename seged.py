def feladat_1() -> list:
    """
    Filebeolvasás
    """
    lista = []
    f = open("kosar.txt","r",encoding="UTF-8")

    for sor in f:
        sor = sor.strip().split()
        for elem in sor:
         #if elem != "F":
             lista.append(elem)


    f.close()

    veglista = []
    for elem in lista:
        l = []
        if elem != "F":
            l.append(elem)


    return veglista


lista = feladat_1()
print(lista)

def feladat_2(lista: list):
    #Ha egyben lenne a lista "F"-enként pici listákat létrehozva amik nem tartalmazzák "F"-et [['toll'],[valami.valami]...
    print("Az összes bevásárlás:",len(lista))


def feladat_3(lista: list):
    sorszam = int(input("Adja meg a vásárlás sorszámát:"))
    #Ha egyben lenne a lista

    index = 0
    for sor in lista:
        if index == sorszam:
            print("A kosár elemeinek száma:",len(sor))
            targy = []
            for elem in sor:
                if elem not in targy:
                    targy.append(elem)
            print("A kosár tartalma: ",targy)

            for i in range(0,len(targy)):
                count = 0
                for elem in sor:
                    if sor[i] == targy[i]:
                        count += 1
                print(count,"-",targy[i])

def feladat_4(lista: list):
    arucikk = input("Adja meg az árucikk nevét:")

    arucikk = arucikk.lower()

    i = 1
    for sor in lista:
        if arucikk in sor.lower():
            print(i,".vásárlásnál vettek először ilyen cikket!")
            break
        i += 1

    j = 1
    for sor in reversed(lista):
        if arucikk in sor.lower():
            print(j,".vásárlásnál vettek utoljára ilyen cikket!")
            break
        j += 1
    db = 0
    for sor in lista:
        if arucikk in sor:
            db += 1
    print(f"Összesen {db} vásárló volt aki ilyen cikket vett")

def feladat_5(lista: list):

    f = open("osszeg.txt","w",encoding="UTF-8")
    targyak = []
    for sor in lista:
        for elem in sor:
            if elem not in targyak:
                targyak.append(elem)
    i = 0
    for sor in lista:
        counter = 0

        for elem in sor:
            if targyak[i] == elem:
                counter += 1000
                f.write(counter+"\n")
    f.close()

