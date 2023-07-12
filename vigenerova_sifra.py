print("Zadejte text k zašifrování: ")
vstup = input()
print("Zadejte heslo: ")
heslo = input()
sifra = ""
for i, znak in enumerate(vstup):
    k = ord(heslo[i % len(heslo)]) - (ord("a") - 1)
    if ord(znak) + k > ord("z"):
        k -= 26
    vysledek = chr(ord(znak) + k)
    sifra += vysledek

print("Výsledek:", sifra)





