#vaja 1
#doma = int(input("koliko golov je dala domača ekipa: "))
#gostje = int(input("vnesi stevilo gostoče ekipe: "))

#print("Domači:", doma)
#print("Gostje:", gostje)
#print("Popravljen rezultat:", doma, ":", gostje)
#print("Skupaj:", doma + gostje)

#vaja 2
#igranje = int(input("koliko minut si igral: "))

#ure = igranje // 60
#inute = igranje % 60 
#dnevi = ure / 24
#print(f"{ure} ur, {minute} minut in {dnevi} dni")

# vaja 3

#dijaki = int(input("Koliko dijakov bo jedlo pice: "))
#cena_pice = float(input("Koliko stane pica: "))

#pice = (dijaki+2)
#skupaj = pice*cena_pice
#vsak = skupaj/dijaki

#print(pice)
#print(skupaj)
#print(vsak)

# vaja 4

starost = int(input("vnesi starost: "))
dan = str(input("kateri dan ste prišli: "))

if starost < 0:
    print("Neveljavna starost.")
else:
    if starost <= 5:
        cena = 0
    elif starost <= 17:
        cena = 5
    elif starost <= 64:
        cena = 8
    else:
        cena = 6

if dan == "torek":
    cena - 2

    print(f"Cena: {cena} EUR")




