import re

zeilen = []
valid_first = 0
valid_second = 0
with open("aoc.txt") as f:
    zeilen = f.readlines()


muster = '([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)'

for i in zeilen:
    match = re.search(muster,i)
    min_anzahl = int(match.group(1))
    max_anzahl = int(match.group(2))
    buchstabe = match.group(3)
    passwort = match.group(4)

    count = passwort.count(buchstabe)
    #Erster Stern
    if count >= min_anzahl and count <= max_anzahl:
        valid_first = valid_first + 1
    #Zweiter Stern
    if passwort[min_anzahl-1] == buchstabe and not passwort[max_anzahl-1] == buchstabe or passwort[max_anzahl-1] == buchstabe and not passwort[min_anzahl-1] == buchstabe:
        valid_second = valid_second + 1

#Ergebnis Erster Stern
print(valid_first)

#Ergebnis Zweiter Stern
print(valid_second)