from Enzymdatabase import getEnzymesDicts
from Southern_current import southernOneEnzyme
from Southern_current import southernTwoEnzymes
from BiologicalCheck import isSizeDifferenceValid

def southernInCbx():
    print("WILDTYPE")
    wt_keylist2, wt_keydict, wt_splitdic, wt_probebindingsites, wt_keyfeatures = southernOneEnzyme()
    print("SINGLE INTEGRATION")
    si_keylist2, si_keydict, si_splitdic, si_probebindingsites, si_keyfeatures = southernOneEnzyme()
    print("MULTIPLE INTEGRATION")
    mi_keylist2, mi_keydict, mi_splitdic, mi_probebindingsites, mi_keyfeatures = southernOneEnzyme()
    print("\nRESULT")

    printed = False
    for i in range(len(wt_keylist2)):
        if wt_keylist2[i] in wt_keydict and wt_keylist2[i] in si_keydict and wt_keylist2[i] in mi_keydict \
                and isSizeDifferenceValid(si_keydict[wt_keylist2[i]]) and isSizeDifferenceValid(mi_keydict[wt_keylist2[i]]):
            enzymes = []
            printResult(i, mi_keydict, si_keydict, wt_keydict, wt_keylist2, enzymes)
            printed = True
    if printed:
        digestionfound = input("Did you found a fitting digestion? y/n\n")

    if not printed or digestionfound == "n":
        wt_keylist4, wt_keydict2, wt_splitdic2 = southernTwoEnzymes(wt_splitdic, wt_probebindingsites, wt_keyfeatures)
        si_keylist4, si_keydict2, si_splitdic2 = southernTwoEnzymes(si_splitdic, si_probebindingsites, si_keyfeatures)
        mi_keylist4, mi_keydict2, mi_splitdic2 = southernTwoEnzymes(mi_splitdic, mi_probebindingsites, mi_keyfeatures)

        finalkeylist = wt_keylist4
        for l in range(len(si_keylist4)):
            if si_keylist4[l] not in finalkeylist:
                finalkeylist.append(si_keylist4[l])
        for n in range(len(mi_keylist4)):
            if mi_keylist4[l] not in finalkeylist:
                finalkeylist.append(mi_keylist4[l])

        for k in range(len(finalkeylist)):
            if finalkeylist[k] in wt_keydict2 and finalkeylist[k] in si_keydict2 and finalkeylist[k] in mi_keydict2:
                if si_keydict2[finalkeylist[k]] and mi_keydict2[finalkeylist[k]] \
                        and isSizeDifferenceValid(si_keydict2[finalkeylist[k]]) \
                        and isSizeDifferenceValid(mi_keydict2[finalkeylist[k]]):
                    enzymes = finalkeylist[k].split("+")
                    onlyOneEnzyme = []; p = "none"
                    printResult(k, mi_keydict2, si_keydict2, wt_keydict2, finalkeylist, enzymes, onlyOneEnzyme, p)
            elif finalkeylist[k] in wt_keydict2 and finalkeylist[k] not in si_keydict2 and finalkeylist[k] not in mi_keydict2:
                enzymes = finalkeylist[k].split("+")
                for m in range(2):
                    if enzymes[m] in mi_keydict and enzymes[m] in si_keydict:
                        onlyOneEnzyme = [si_keydict[enzymes[m]], mi_keydict[enzymes[m]]]
                        if wt_keydict2[finalkeylist[k]] \
                                and isSizeDifferenceValid(wt_keydict2[finalkeylist[k]]) and isSizeDifferenceValid(onlyOneEnzyme[0]) and isSizeDifferenceValid(onlyOneEnzyme[1]):
                            p = "wt"
                            printResults(k, mi_keydict2, si_keydict2, wt_keydict2, finalkeylist, enzymes, onlyOneEnzyme, p)
            elif finalkeylist[k] not in wt_keydict2 and finalkeylist[k] in mi_keydict2 and finalkeylist[k] in si_keydict2:
                enzymes = finalkeylist[k].split("+")
                for m in range(2):
                    if enzymes[m] in wt_keydict:
                        onlyOneEnzyme = wt_keydict[enzymes[m]]
                        if si_keydict2[finalkeylist[k]] and mi_keydict2[finalkeylist[k]] \
                                and isSizeDifferenceValid(si_keydict2[finalkeylist[k]]) and isSizeDifferenceValid(mi_keydict2[finalkeylist[k]]) and isSizeDifferenceValid(onlyOneEnzyme):
                            p = "si+mi"
                            printResults(k, mi_keydict2, si_keydict2, wt_keydict2, finalkeylist, enzymes, onlyOneEnzyme, p)


def printResult(index, mi_keydict, si_keydict, wt_keydict, keyList, enzymes, onlyOneEnzyme, p):
    JoergsEnzymes, TopEnzymes = getEnzymesDicts()
    if not enzymes:
        print(keyList[index])
    else:
        print(enzymes[0], "+", enzymes[1])

    if not onlyOneEnzyme:
        print("resulting bands for wildtype:", wt_keydict[keyList[index]])
        print("resulting bands for single integration:", si_keydict[keyList[index]])
        print("resulting bands for multiple integration:", mi_keydict[keyList[index]])
    elif p == "wt":
        print("resulting bands for wildtype:", wt_keydict[keyList[index]])
        print("resulting bands for single integration:", onlyOneEnzyme[0])
        print("resulting bands for multiple integration:", onlyOneEnzyme[1])
    elif p == "si+mi":
        print("resulting bands for wildtype:", onlyOneEnzyme)
        print("resulting bands for single integration:", si_keydict[keyList[index]])
        print("resulting bands for multiple integration:", mi_keydict[keyList[index]])

    if not enzymes:
        print("binding site:", JoergsEnzymes[keyList[index]][0])
        print(JoergsEnzymes[keyList[index]][1], "ends")
        print("buffer:", JoergsEnzymes[keyList[index]][2])
        print("temperature:", JoergsEnzymes[keyList[index]][3])
        print("\n")
    else:
        print("binding site of", enzymes[0], ":", JoergsEnzymes[enzymes[0]][0])
        print("binding site of", enzymes[1], ":", JoergsEnzymes[enzymes[1]][0])
        print(enzymes[0], "has", JoergsEnzymes[enzymes[0]][1], "ends")
        print(enzymes[1], "has", JoergsEnzymes[enzymes[1]][1], "ends")
        buffers1 = JoergsEnzymes[enzymes[0]][2].split("/")
        buffers2 = JoergsEnzymes[enzymes[1]][2].split("/")
        if "CS" in buffers1 and "CS" in buffers2:
            print("buffer: CS")
        elif "3.1" in buffers1 and "3.1" in buffers2:
            print("buffer: 3.1")
        elif "2.1" in buffers1 and "2.1" in buffers2:
            print("buffer: 2.1")
        else:
            print("Please select the suitable buffer manually")
            print("buffers of", enzymes[0], ":", JoergsEnzymes[enzymes[0]][2])
            print("buffers of", enzymes[1], ":", JoergsEnzymes[enzymes[1]][2])
        if JoergsEnzymes[enzymes[0]][3] == "37 °C" and JoergsEnzymes[enzymes[1]][3] == "37 °C":
            print("temperature: 37 °C")
        elif JoergsEnzymes[enzymes[0]][3] == "50 °C" and JoergsEnzymes[enzymes[1]][3] == "50 °C":
            print("temperature: 50 °C")
        else:
            print("Digestion has to be done in two steps with following temperatures:",
                  JoergsEnzymes[enzymes[0]][3], ",", JoergsEnzymes[enzymes[1]][3])
        print("\n")
