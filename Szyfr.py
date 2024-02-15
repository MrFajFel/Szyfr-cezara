# Szyfr Cezara
tekst = input("Wpisz wiadomosc: ")
szyfr = ''
for char in tekst:
    if not char.isalpha():
        continue
    kod = ord(char) + 3
    szyfr += chr(kod)

print(szyfr)
