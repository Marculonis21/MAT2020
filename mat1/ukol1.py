#!/usr/bin/env python3

f6a = open("m_6a.csv")
f6b = open("m_6b.csv")
f6c = open("m_6c.csv")

linesA = f6a.readlines()
linesB = f6b.readlines()
linesC = f6c.readlines()

f6a.close()
f6b.close()
f6c.close()

linesA = [x for x in linesA if not "student" in x or x == " "]
linesB = [x for x in linesB if not "student" in x or x == " "]
linesC = [x for x in linesC if not "student" in x or x == " "]

classA = []
classB = []
classC = []

for i in range(len(linesA)):
    change = list(linesA[i])
    if(change[-1] == '\n'):
        change.pop()
        linesA[i] = "".join(change)
    classA.append(linesA[i].split(',',2))

for i in range(len(linesB)):
    change = list(linesB[i])
    if(change[-1] == '\n'):
        change.pop()
        linesB[i] = "".join(change)
    classB.append(linesB[i].split(',',2))

for i in range(len(linesC)):
    change = list(linesC[i])
    if(change[-1] == '\n'):
        change.pop()
        linesC[i] = "".join(change)
    classC.append(linesC[i].split(',',2))

matA = {}
for prijmeni,jmeno,mat in classA:
    for sub in mat.split(','):
        if not(sub == ''):
            try:
                matA[sub].append("{} {}".format(prijmeni,jmeno))
            except KeyError:
                matA[sub] = ["{} {}".format(prijmeni,jmeno)]

matB = {}
for prijmeni,jmeno,mat in classB:
    for sub in mat.split(','):
        if not(sub == ''):
            try:
                matB[sub].append("{} {}".format(prijmeni,jmeno))
            except KeyError:
                matB[sub] = ["{} {}".format(prijmeni,jmeno)]

matC = {}
for prijmeni,jmeno,mat in classC:
    for sub in mat.split(','):
        if not(sub == ''):
            try:
                matC[sub].append("{} {}".format(prijmeni,jmeno))
            except KeyError:
                matC[sub] = ["{} {}".format(prijmeni,jmeno)]

      
print("6.A")

for sub in matA:
    names = ""
    for index, name in enumerate(matA[sub]):
        names += name
        if(index < len(matA[sub]) - 1):
            names += ", "

    print("Předmět: {} ({}):\n{}".format(sub, len(matA[sub]), names))
    matA[sub].append(len(matA[sub]))

print()
print("6.B")
for sub in matB:
    print(sub)
    
    names = ""
    for index, name in enumerate(matB[sub]):
        names += name
        if(index < len(matB[sub]) - 1):
            names += ", "

    print("Předmět: {} ({}):\n{}".format(sub, len(matB[sub]), names))
    matB[sub].append(len(matB[sub]))

print()
print("6.C")
for sub in matC:
    names = ""
    for index, name in enumerate(matC[sub]):
        names += name
        if(index < len(matC[sub]) - 1):
            names += ", "

    print("Předmět: {} ({}):\n{}".format(sub, len(matC[sub]), names))
    matC[sub].append(len(matC[sub]))

print()
print("předmět | 6.A | 6.B | 6.C | celkem\n--------|-----|-----|-----|-------")

subAll = {}
for sub in matA:
    try:
        subAll[sub] += int(matA[sub][-1])
    except KeyError:
        subAll[sub] = int(matA[sub][-1])

for sub in matB:
    try:
        subAll[sub] += int(matB[sub][-1])
    except KeyError:
        subAll[sub] = int(matB[sub][-1])

for sub in matC:
    try:
        subAll[sub] += int(matC[sub][-1])
    except KeyError:
        subAll[sub] = int(matC[sub][-1])


for s in subAll:
    print("{:8}".format(s), end="|")
    try:
        print("{:4} ".format(matA[s][-1]), end="|")
    except KeyError:
        print("   0 ", end="|")

    try:
        print("{:4} ".format(matB[s][-1]), end="|")
    except KeyError:
        print("   0 ", end="|")

    try:
        print("{:4} ".format(matC[s][-1]), end="|")
    except KeyError:
        print("   0 ", end="|")

    print("{:4} ".format(subAll[s]), end="|")
    print()
