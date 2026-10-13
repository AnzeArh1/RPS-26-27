import requests as r
# 1.naloga

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

def v_tujo():
    znesek = float(input("vnesi znesek v EUR: "))
    valuta = input("vnesi v katero valuto bi pretvoril:")
    valuta =  valuta.upper()
    if valuta not in a["rates"]:
        print(f"valuta [valuta] ne obstaja")
    else:
        print(f"round(a["rates"][valuta]"znesek, 2)) (valuta)= 





def main():
    fran = r.get(https://api.frankfurter.dev/v1/latest)
    franJSON = fran.JSON()
    vaja1(franJSON)


if __name__ == '__main__':
    main()