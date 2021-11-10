from Enzymdatabase import getEnzymesDicts
from Southern_current import southernOneEnzyme
from Southern_current import southernTwoEnzymes
from BiologicalCheck import isSizeDifferenceValid


def southernInLocus():
    print("WILDTYPE")
    wt_keylist2, wt_keydict, wt_splitdic, wt_probebindingsites, wt_keyfeatures = southernOneEnzyme()
    print("MUTATION")
    mut_keylist2, mut_keydict, mut_splitdic, mut_probebindingsites, mut_keyfeatures = southernOneEnzyme()

    print("\nRESULT")

    printed = False
    for i in range(len(wt_keylist2)):
        if wt_keylist2[i] in wt_keydict and wt_keylist2[i] in mut_keydict and mut_keydict[wt_keylist2[i]] \
                and isSizeDifferenceValid(wt_keydict[wt_keylist2[i]]) and isSizeDifferenceValid(mut_keydict[wt_keylist2[i]]) \
                and (len(wt_keydict[wt_keylist2[i]]) == len(mut_keydict[wt_keylist2[i]]) > 1 or len(mut_keydict[wt_keylist2[i]]) != len(wt_keydict[wt_keylist2[i]])):
            enzymes = []; onlyOneEnzyme = []; p = "none"
            printResults(i, mut_keydict, wt_keydict, wt_keylist2, enzymes, onlyOneEnzyme, p)
            printed = True
    if printed:
        digestionfound = input("Did you found a fitting digestion? y/n\n")

    if not printed or digestionfound == "n":
        wt_keylist4, wt_keydict2, wt_splitdic2 = southernTwoEnzymes(wt_splitdic, wt_probebindingsites, wt_keyfeatures)
        mut_keylist4, mut_keydict2, mut_splitdic2 = southernTwoEnzymes(mut_splitdic, mut_probebindingsites, mut_keyfeatures)

        finalkeylist = wt_keylist4
        for k in range(len(mut_keylist4)):
            if mut_keylist4[k] not in finalkeylist:
                finalkeylist.append(mut_keylist4[k])
        finalkeylist.sort()

        for j in range(len(finalkeylist)):
            if finalkeylist[j] in wt_keydict2 and finalkeylist[j] in mut_keydict2:
                if wt_keydict2[finalkeylist[j]] and mut_keydict2[finalkeylist[j]] \
                        and isSizeDifferenceValid(wt_keydict2[finalkeylist[j]]) and isSizeDifferenceValid(mut_keydict2[finalkeylist[j]]) \
                        and (len(wt_keydict2[finalkeylist[j]]) == len(mut_keydict2[finalkeylist[j]]) > 1 or len(wt_keydict2[finalkeylist[j]]) != len(mut_keydict2[finalkeylist[j]])):
                    enzymes = finalkeylist[j].split("+")
                    onlyOneEnzyme = []; p = "none"
                    printResults(j, mut_keydict2, wt_keydict2, finalkeylist, enzymes, onlyOneEnzyme, p)
            elif finalkeylist[j] in wt_keydict2 and finalkeylist[j] not in mut_keydict2:
                enzymes = finalkeylist[j].split("+")
                for m in range(2):
                    if enzymes[m] in mut_keydict:
                        onlyOneEnzyme = mut_keydict[enzymes[m]]
                        if wt_keydict2[finalkeylist[j]] \
                                and isSizeDifferenceValid(wt_keydict2[finalkeylist[j]]) and isSizeDifferenceValid(onlyOneEnzyme) \
                                and (len(wt_keydict2[finalkeylist[j]]) == len(onlyOneEnzyme) > 1 or len(wt_keydict2[finalkeylist[j]]) != len(onlyOneEnzyme)):
                            p = "wt"
                            printResults(j, mut_keydict2, wt_keydict2, finalkeylist, enzymes, onlyOneEnzyme, p)
            elif finalkeylist[j] not in wt_keydict2 and finalkeylist[j] in mut_keydict2:
                enzymes = finalkeylist[j].split("+")
                for m in range(2):
                    if enzymes[m] in wt_keydict:
                        onlyOneEnzyme = wt_keydict[enzymes[m]]
                        if mut_keydict2[finalkeylist[j]] \
                                and isSizeDifferenceValid(mut_keydict2[finalkeylist[j]]) and isSizeDifferenceValid(onlyOneEnzyme) \
                                and (len(mut_keydict2[finalkeylist[j]]) == len(onlyOneEnzyme) > 1 or len(mut_keydict2[finalkeylist[j]]) != len(onlyOneEnzyme)):
                            p = "mut"
                            printResults(j, mut_keydict2, wt_keydict2, finalkeylist, enzymes, onlyOneEnzyme, p)

def printResults(index, mut_keydict, wt_keydict, keyList, enzymes, onlyOneEnzyme, p):
    JoergsEnzymes, TopEnzymes = getEnzymesDicts()
    if not enzymes:
        print(keyList[index])
    else:
        print(enzymes[0], "+", enzymes[1])

    if not onlyOneEnzyme:
        print("resulting bands for wildtype", wt_keydict[keyList[index]])
        print("resulting bands for mutation", mut_keydict[keyList[index]])
    elif p == "wt":
        print("resulting bands for wildtype", wt_keydict[keyList[index]])
        print("resulting bands for mutation", onlyOneEnzyme)
    elif p == "mut":
        print("resulting bands for wildtype", onlyOneEnzyme)
        print("resulting bands for mutation", mut_keydict[keyList[index]])

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
