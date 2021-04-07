import time
print("Questo programma serve a calcolare qual è la tua versione preferita di windows classico.")
print()
versioni = ["1.x", "2.x", "3.x for workgroups", "3.x non-for workgroups", "95", "98", "ME", "NT 3.x", "NT 4.x", "2000", "XP"]
daCancellare = []

def rispostaAffermativa(prompt):
    return input(prompt).lower()[0] in ("s", "y")
def cancellaSeCe(lista, elem):
    ls2 = lista[:]
    while elem in ls2:
        ls2.remove(elem)
    return ls2

if rispostaAffermativa("Ti piacciono i colori? "):
    daCancellare.append("1.x")
else:
    print("\nPer te va bene Windows 1.x")
    input("\nPremi un tasto per uscire...\n")
    raise SystemExit

if rispostaAffermativa("Ti piacciono le alte risoluzioni? "):
    daCancellare.append("1.x")
    daCancellare.append("2.x")
    daCancellare.append("3.x")
else:
    daCancellare.append("95")
    daCancellare.append("98")
    daCancellare.append("ME")
    daCancellare.append("NT 4.x")
    daCancellare.append("2000")
    daCancellare.append("XP")
if rispostaAffermativa("Ti piace stare a casa? "):
    daCancellare.append("NT 3.x")
    daCancellare.append("NT 4.x")
    daCancellare.append("2000")
    daCancellare.append("3.x for workgroups")
else:
    daCancellare.append("1.x")
    daCancellare.append("2.x")
    daCancellare.append("3.x non-for workgroups")
    daCancellare.append("95")
    daCancellare.append("98")
    daCancellare.append("ME")
if rispostaAffermativa("Ti piace l'idea di lavorare con lo stesso pc a casa e in ufficio? "):
    daCancellare.append("1.x")
    daCancellare.append("2.x")
    daCancellare.append("3.x non-for workgroups")
    daCancellare.append("95")
    daCancellare.append("98")
    daCancellare.append("ME")
    daCancellare.append("NT 3.x")
    daCancellare.append("NT 4.x")
    daCancellare.append("2000")
    daCancellare.append("3.x for workgroups")
else:
    daCancellare.append("XP")

if rispostaAffermativa("Ti piace l'idea di usare solo quei pochi programmi inclusi con win? "):
    daCancellare.append("95")
    daCancellare.append("98")
    daCancellare.append("ME")
    daCancellare.append("2000")
    daCancellare.append("XP")
else:
    daCancellare.append("1.x")
    daCancellare.append("2.x")
    daCancellare.append("3.x for workgroups")
    daCancellare.append("3.x non-for workgroups")
    daCancellare.append("NT 3.x")
    daCancellare.append("NT 4.x")
if rispostaAffermativa("Ti piace il vero MS-DOS? "):
    daCancellare.append("NT 3.x")
    daCancellare.append("NT 4.x")
    daCancellare.append("ME")
    daCancellare.append("2000")
    daCancellare.append("XP")
else:
    daCancellare.append("1.x")
    daCancellare.append("2.x")
    daCancellare.append("3.x for workgroups")
    daCancellare.append("3.x non-for workgroups")
    daCancellare.append("95")
    daCancellare.append("98")
if rispostaAffermativa("Ti piace la BSoD? "):
    daCancellare.append("1.x")
    daCancellare.append("2.x")
    daCancellare.append("3.x for workgroups")
    daCancellare.append("3.x non-for workgroups")
    daCancellare.append("NT 3.x")
    daCancellare.append("NT 4.x")
    daCancellare.append("2000")
    daCancellare.append("XP")
else:
    daCancellare.append("98")
    daCancellare.append("95")
    daCancellare.append("ME")

print("\nSto elaborando i dati.... ")
for vers in daCancellare:
    versioni = cancellaSeCe(versioni, vers)
    time.sleep(0.5)
    print("Still working")
print("fatto")

if len(versioni) == 0:
    print("Mister Gusti Difficili, per te non va bene nulla.")
    input("\nPremi un tasto per uscire...\n")
    raise SystemExit
else:
    print("\nPer te vanno bene queste versioni: \n")
    for x in versioni: print("Windows "+x)
    input("\nPremi un tasto per uscire...\n")
    raise SystemExit
