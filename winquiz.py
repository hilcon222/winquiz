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

if rispostaAffermativa("Do you like colors? "):
    daCancellare.append("1.x")
else:
    print("\nFor you, Windows 1.x")
    input("\nPress a key to exit...\n")
    raise SystemExit

if rispostaAffermativa("Do you like high resolutions? "):
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
if rispostaAffermativa("Do you like staying at home? "):
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
if rispostaAffermativa("Do you want to work at home and in the office with the same PC? "):
    daCancellare.append("1.x")
    daCancellare.append("2.x")
    daCancellare.append("3.x not-for workgroups")
    daCancellare.append("95")
    daCancellare.append("98")
    daCancellare.append("ME")
    daCancellare.append("NT 3.x")
    daCancellare.append("NT 4.x")
    daCancellare.append("2000")
    daCancellare.append("3.x for workgroups")
else:
    daCancellare.append("XP")

if rispostaAffermativa("Do you use only programs included with Windows, usually? "):
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
if rispostaAffermativa("Do you like the original, old Ms-dos (16-bit text mode Microsoft system)? "):
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
if rispostaAffermativa("Do you like blue screen of death? "):
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

print("\nWorking.... ")
for vers in daCancellare:
    versioni = cancellaSeCe(versioni, vers)
print("done")

if len(versioni) == 0:
    print("I cannot find the correct version for you. Try Windows 10.")
    input("\nPress a key to exit...\n")
    raise SystemExit
else:
    print("\nVersions: \n")
    for x in versioni: print("Windows "+x)
    input("\nPress a key to exit...\n")
    raise SystemExit
