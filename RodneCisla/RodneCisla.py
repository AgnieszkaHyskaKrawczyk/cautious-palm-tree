import random
print('Falšovač rodných čísel')
dd = input("Vložte den narození: ")
mm = input("Vložte měsíc narození: ")
yy = input("Vložte rok narození: ")
rr = random.randint(1000, 9999)

print("Rodné číslo: " + str(yy + mm + dd) + "/" + str(rr))
#

print('Trojúhelník')
alfa = int(input('Zadejte úhel alfa = '))
beta = int(input('Zadejte úhel beta = '))
gamma = int(input('Zadejte úhel gamma = '))

sum = str(alfa + beta + gamma)

if sum == '180':
    print('Bravo! Je to trojúhelník')
else:
    print('To neni trojúhelník!!')
#

print('Dny v měsíci')
m = input('Zadej číslo měsíce v roce (1-12): ')
if m == '1':
    print('Leden ma 31 dní')
elif m == '2':
    print('Unor ma 28 dní')
elif m == '3':
    print('Brezen ma 31 dní')
elif m == '4':
    print('Duben ma 30 dní')
elif m == '5':
    print('Kveten ma 31 dní')
elif m == '6':
    print('Cerven ma 30 dní')
elif m == '7':
    print('Cervenec ma 31 dní')
elif m == '8':
    print('Srpen ma 31 dní')
elif m == '9':
    print('Zari ma 30 dní')
elif m == '10':
    print('Rijen ma 31 dní')
elif m == '11':
    print('Listopad ma 30 dní')
elif m == '12':
    print('Prosinec ma 31 dní')
else:
    print('Dalsi mesice nejsou')
#

print('Největší ze tří')
prvni = int(input('Zadejte prvni číslo = '))
druhe = int(input('Zadejte druhe číslo = '))
treti = int(input('Zadejte treti číslo = '))

if prvni < druhe:
    if druhe < treti:
        print('Největší je číslo = ' + str(treti))
    else:
        print('Největší je číslo = ' + str(druhe))
elif treti < prvni:
    print('Největší je číslo = ' + str(prvni))
#

print('Stupně vítězů')
prvni = input('Zadejte jméno prvniho plavce = ')
druhy = input('Zadejte jméno druheho plavce = ')
treti = input('Zadejte jméno tretiho plavce = ')

casPrvniho = random.randint(45, 60)
casDruheho = random.randint(45, 60)
casTretiho = random.randint(45, 60)

if casPrvniho < casDruheho:
    if casPrvniho < casTretiho:
        z = casPrvniho
        print('Zlatou medaili získal ' + prvni + ' s časem ' + str(casPrvniho))
        if casDruheho < casTretiho:
            print('Stříbrnou medaili získal ' + druhy + ' s časem ' + str(casDruheho))
            print('Bronzovou medaili získal ' + treti + ' s časem ' + str(casTretiho))
        else:
            print('Stříbrnou medaili získal ' + treti + ' s časem ' + str(casTretiho))
            print('Bronzovou medaili získal ' + druhy + ' s časem ' + str(casDruheho))
    else:
        print('Zlatou medaili získal ' + treti + ' s časem ' + str(casTretiho))
else:
    if casDruheho < casTretiho:
        print('Zlatou medaili získal ' + druhy + ' s časem ' + str(casDruheho))
        if casPrvniho < casTretiho:
            print('Stříbrnou medaili získal ' + prvni + ' s časem ' + str(casPrvniho))
            print('Bronzovou medaili získal ' + treti + ' s časem ' + str(casTretiho))
        else:
            print('Stříbrnou medaili získal ' + treti + ' s časem ' + str(casTretiho))
            print('Bronzovou medaili získal ' + prvni + ' s časem ' + str(casPrvniho))

#
##   ##         #
print('Částka slovně')
slovnikSto = [['1', 'sto'], ['2', 'dvě stě'], ['3', 'tři sta'], ['4', 'čtyři sta'], ['5', 'pět set'], ['6', 'šest set'], ['7', 'sedm set'], ['8', 'osm set'], ['9', 'devět set']]
slovnikDeset = [['10', '10 deset'], ['11', 'jedenáct'], ['12', 'dvanáct'], ['13', 'třináct'], ['14', 'čtrnáct'], ['15', 'patnáct'], ['16', 'šestnáct'], ['17', 'sedmnáct'], ['18', 'osmnáct'], ['19', 'devatenáct']]
slovnikDesitek = [['2', 'dvacet'], ['3', 'třicet'], ['4', 'čtyřicet'], ['5', 'padesát'], ['6', 'šedesát'], ['7', 'sedmdesát'], ['8', 'osmdesát'], ['9', 'devadesát']]
slovnikJeden = [['1', 'jedna'], ['2', 'dva'], ['3', 'tři'], ['4', 'čtyři'], ['5', 'pět'], ['6', 'šest'], ['7', 'sedm'], ['8', 'osm'], ['9', 'devět']]
castka = input('Zadejte třícifernou částku v korunách: ')
print(castka)

for i in range(len(slovnikSto)):
    for j in range(len(slovnikSto[i])):
        if castka[0] == slovnikSto[i][0]:
            print(slovnikSto[i][1])
            break;

for k in range(len(slovnikDeset)):
    for l in range(len(slovnikDeset[k])):
        if castka[1] == '1':
            x = castka[1] + castka[2]
            if (x == slovnikDeset[k][0]):
                print(slovnikDeset[k][1])
                break;
        elif castka[1] == '0':
            continue;
        
for m in range(len(slovnikDesitek)):
   for n in range(len(slovnikDesitek[m])):
       if castka[1] == slovnikDesitek[m][0]:
           print(slovnikDesitek[m][1])
           break;

for o in range(len(slovnikJeden)):
    for p in range(len(slovnikJeden[o])):
        if castka[2] == slovnikJeden[o][0]:
            if castka[1] != '1':
                print(slovnikJeden[o][1])
                break;
            else:
                break;

###########3
print("Přechylování příjmení")
surnames = ['Novák', 'Dvořák', 'Kolář', 'Eliáš', 'Čermák', 'Kalous']
for surname in surnames:
    print(surname + "ová")

##########3
print("Vyznamenání")
grades = [
  ['Josef Novák', 1.65],
  ['Martin Dvořák', 1.44],
  ['Kateřina Kolářová', 1.15],
  ['Kryštof Eliáš', 1.11], 
  ['Ludmila Čermáková', 1.24], 
  ['Miroslav Kalous', 1.98],
  ['Jaromír Ježek', 1.28],
  ['Kristýna Slezáková', 1.35],
  ['Igor Rosický', 1.05],
  ['Lenka Zdražilová', 1.39]
]
for r in range(len(grades)):
    for s in range(len(grades[r])):
        if grades[r][1] <= 1.2:
            print(grades[r][0] + " pochvala")
        elif grades[r][1] <= 1.4: 
            print(grades[r][0] + " vyznamenání")
        else:
            print(grades[r][0] + " NIC")
#######
######
print("Teploty 2017")
temps = [-5.6, 1.1, 5.9, 6.9, 13.8, 18.2, 18.5, 18.8, 11.8, 9.5, 3.7, 0.8]
z = 0
for t in range(len(temps)):
    if temps[t] < 4:
        z = z + 1

print("Průměrná teplota kelsla pod 4 stupně Celsia v " + str(z) + " měsících")

            

      


                 













