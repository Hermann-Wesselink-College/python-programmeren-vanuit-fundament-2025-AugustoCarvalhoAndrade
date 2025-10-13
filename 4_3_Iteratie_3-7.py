# Opgave 3 tot en met 7 van paragraaf 4.3
getal = int(input("Van welk getal wil je de tafel?"))
if getal <= 0 or getal > 10:
    print("Error")
else:
 for i in range(1,11):
    print(str(i) + " keer " + str(getal) + " = " + str(i * getal))

# opdracht 4
mile = 1.609
print("Km\tMiles")
for i in range(1,11):
    miles = i * mile
print(str(i) + "\t" + str(miles))

# opdracht 5
getal = int(input("Van welk getal wil je de faculteit?"))
uitkomst = 1
for i in range(1, getal + 1):
  uitkomst = uitkomst * i
 
print(str(uitkomst))

# opdracht 6
for i in range(0,50,2):
  print(i)

# opdracht 7
minPlus = False
uitkomst = 1
 
for i in range(3,100000,2):
  if minPlus:
    uitkomst = uitkomst + (1/i)
  else:
    uitkomst = uitkomst - (1/i)
  minPlus = not minPlus
 
print(4*uitkomst)