import requests as r
# 1.naloga
"""
fran = r.get(https://api.frankfurter.dev/v1/latest)
klicJSON = fran.JSON

def vaja1():
    l=["USD", "GBP", "CHF", "JPY"]
    i = 0
    if b.status_code == 200:
        print(F"tečaji na dan (a["date])")
    while i < 4:
        print(franJSON["rates[l[x]]"])
        i+=1
        print(f"skupaj valut[i]")
    else:
        print("napaka")
"""
# 2. naloga
"""
def v_tujo():
    znesek = float(input("vnesi znesek v EUR: "))
    valuta = input("vnesi v katero valuto bi pretvoril:")
    valuta =  valuta.upper()
    if valuta not in a["rates"]:
        print(f"valuta [valuta] ne obstaja")
    else:
        print(f"round(a["rates"][valuta]"znesek, 2)) (valuta)= 
def v_evre():
    znesek = float(input("vnesi znesek v EUR: "))
    valuta = input("Vnesi v katero valuto bi pretvoril: ")
    valuta = valuta.upper()
    if valuta not in a["rates"]:
        print(f"Valuta[valuta] ne obstaja")
    else:
        print(f{round(a[rates][valuta]*mult,0)}") {valuta} = {a["amount"]* multd} eur")
"""
# 3. naloga
"""
def vaja_3():
    i=0
    print(a["rates"][1])
    while i < 7:

        i +=1
"""
url = "https://api.frankfurter.dev/v1/2026-09-01..2026-09-07"
podatki =  requests.get(url, params={"symbols": "USD"}).json()
dnevi = podatki["rates"]

datumi = list(dnevi.keys())
print(datumi[0] + ":", dnevi[datumi[0]]["USD"])

for i in range(1, len(datumi)):
    danes = dnevi[datumi[i]]["USD"]
    vceraj = dnevi[datumi[i - 1]]["USD"]

if danes > vceraj:
    smer = "Gor"
else:
    smer = "dol"

print(datumi[i] + ":", danes, "(" + smer + ")")
print("Podatki od", datumi[0], "do", datumi[-1] + ", skupaj", len(datumi), "dni")








def main():
   # fran = r.get(https://api.frankfurter.dev/v1/latest)
  #  franJSON = fran.JSON()
   # vaja1(franJSON)


if __name__ == '__main__':
    main()