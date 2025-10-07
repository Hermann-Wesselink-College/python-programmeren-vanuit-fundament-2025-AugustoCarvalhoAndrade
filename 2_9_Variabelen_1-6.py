# opdrachten 1 tot en met 6 van paragraaf 2.9
totaalprijs = 50.00
kortingsBon = 7.50
nieuwe_prijs = totaalprijs - kortingsBon
print("Nieuwe prijs:", nieuwe_prijs)

# opdracht 2
cijfer1 = 8
cijfer2 = 6
gemiddelde = (cijfer1 + cijfer2) / 2
print("Het gemiddelde is:", gemiddelde)

# opdracht 3
prijsExclBtw = float(input("Voer het bedrag exclusief btw in: "))
prijsInclBtw = prijsExclBtw * 1.21
print("Prijs inclusief 21% btw:", prijsInclBtw)

# opdracht 4
totaalprijs = float(input("Totaalprijs van de producten:"))
verzendkosten = 3.95
teBetalen = totaalprijs + verzendkosten
print("Totaalprijs: " + str(totaalprijs) + " EUR.")
print("Verzendkosten: " + str(verzendkosten) + " EUR.")
print("TOTAAL: " + str(teBetalen) + " EUR.")

# opdracht 5
bedrag = float(input("Voer een bedrag in euros in"))
wisselkoers = 1.1648
prijsDollar = bedrag * wisselkoers
print("$" + str(prijsDollar))

# opdracht 6
totaalPrijs = float(input("Geef een totaalprijs:"))
kortingsPercentage = float(input("Geef een kortingspercentage:"))
nieuwePrijs = (1 - (kortingsPercentage / 100)) * totaalPrijs
print(nieuwePrijs)