# Opdracht 1 tot en met 7 van pragraaf 2.10
from datetime import datetime
datum = datetime.now()
maand = datum.month
print(str(maand))

# opdracht 2
from datetime import datetime
datum = datetime.now()
dag = datum.day
print(str(dag))

# opdracht 3
from datetime import datetime
datum = datetime.now()
dag = datum.day
maand = datum.month
jaar = datum.year
print(str(dag) + "-" + str(maand) + "-" + str(jaar))

# opdracht 4
from datetime import datetime
datumtijd = datetime.now()
minuut = datumtijd.minute
print(str(minuut))

# opdracht 5
from datetime import datetime
datumtijd = datetime.now()
minuut = datumtijd.minute
uur = datumtijd.hour
print(str(uur) + ":" + str(minuut))

# opdracht 6
from datetime import datetime
datumtijd = datetime.now()
minuut = datumtijd.minute
uur = datumtijd.hour
dag = datumtijd.day
maand = datumtijd.month
jaar = datumtijd.year
 
datum = str(dag) + "-" + str(maand) + "-" + str(jaar)
tijd = str(uur) + ":" + str(minuut)
 
print("De datum van vandaag is " + datum + ". Het is nu " + tijd + ".")

# opdracht 7 a
from datetime import datetime
d0 = datetime(2017, 9, 11)
d1 = datetime(1988, 3, 19)
verschil = d0 - d1
print(verschil.days)
# b
from datetime import datetime
d0 = datetime.now()
d1 = datetime(1988, 3, 17)
verschil = d0 - d1
print(verschil.days)
# c
from datetime import datetime
d0 = datetime.now()
d1 = datetime(1988, 3, 17)
datumVerschil = d0 - d1
dagenVerschil = datumVerschil.days / 365.25
print(dagenVerschil)