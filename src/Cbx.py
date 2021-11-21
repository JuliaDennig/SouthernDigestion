from Enzymdatabase import get_enzymes_dicts
from Southern_current import southern_one_enzyme
from Southern_current import southern_two_enzymes
from BiologicalCheck import is_size_difference_valid

def print_results(index, mi_keydict, si_keydict, wt_keydict, keyList, enzymes, only_one_enzyme, p):
    MYENZYMES, TOPENZYMES = get_enzymes_dicts()
    if not enzymes:
        print(keyList[index])
    else:
        print(enzymes[0], "+", enzymes[1])

    if not only_one_enzyme:
        print("resulting bands for wildtype:", wt_keydict[keyList[index]])
        print("resulting bands for single integration:", si_keydict[keyList[index]])
        print("resulting bands for multiple integration:", mi_keydict[keyList[index]])
    elif p == "wt":
        print("resulting bands for wildtype:", wt_keydict[keyList[index]])
        print("resulting bands for single integration:", only_one_enzyme[0])
        print("resulting bands for multiple integration:", only_one_enzyme[1])
    elif p == "si+mi":
        print("resulting bands for wildtype:", only_one_enzyme)
        print("resulting bands for single integration:", si_keydict[keyList[index]])
        print("resulting bands for multiple integration:", mi_keydict[keyList[index]])

    if not enzymes:
        print("binding site:", MYENZYMES[keyList[index]][0])
        print(MYENZYMES[keyList[index]][1], "ends")
        print("buffer:", MYENZYMES[keyList[index]][2])
        print("temperature:", MYENZYMES[keyList[index]][3])
        print("\n")
    else:
        print("binding site of", enzymes[0], ":", MYENZYMES[enzymes[0]][0])
        print("binding site of", enzymes[1], ":", MYENZYMES[enzymes[1]][0])
        print(enzymes[0], "has", MYENZYMES[enzymes[0]][1], "ends")
        print(enzymes[1], "has", MYENZYMES[enzymes[1]][1], "ends")
        buffers1 = MYENZYMES[enzymes[0]][2].split("/")
        buffers2 = MYENZYMES[enzymes[1]][2].split("/")
        if "CS" in buffers1 and "CS" in buffers2:
            print("buffer: CS")
        elif "3.1" in buffers1 and "3.1" in buffers2:
            print("buffer: 3.1")
        elif "2.1" in buffers1 and "2.1" in buffers2:
            print("buffer: 2.1")
        else:
            print("Please select the suitable buffer manually")
            print("buffers of", enzymes[0], ":", MYENZYMES[enzymes[0]][2])
            print("buffers of", enzymes[1], ":", MYENZYMES[enzymes[1]][2])
        if MYENZYMES[enzymes[0]][3] == "37 °C" and MYENZYMES[enzymes[1]][3] == "37 °C":
            print("temperature: 37 °C")
        elif MYENZYMES[enzymes[0]][3] == "50 °C" and MYENZYMES[enzymes[1]][3] == "50 °C":
            print("temperature: 50 °C")
        else:
            print("Digestion has to be done in two steps with following temperatures:",
                  MYENZYMES[enzymes[0]][3], ",", MYENZYMES[enzymes[1]][3])
        print("\n")

def southern_in_cbx():
    print("WILDTYPE")
    wt_keylist2, wt_keydict, wt_splitdic, wt_probe_bindingsites, wt_keyfeatures = southern_one_enzyme()
    print("SINGLE INTEGRATION")
    si_keylist2, si_keydict, si_splitdic, si_probe_bindingsites, si_keyfeatures = southern_one_enzyme()
    print("MULTIPLE INTEGRATION")
    mi_keylist2, mi_keydict, mi_splitdic, mi_probe_bindingsites, mi_keyfeatures = southern_one_enzyme()
    print("\nRESULT")

    printed = False
    for i in range(len(wt_keylist2)):
        if wt_keylist2[i] in wt_keydict and wt_keylist2[i] in si_keydict and wt_keylist2[i] in mi_keydict \
                and is_size_difference_valid(si_keydict[wt_keylist2[i]]) and is_size_difference_valid(mi_keydict[wt_keylist2[i]]):
            enzymes, only_one_enzyme = [], []
            p = "none"
            print_results(i, mi_keydict, si_keydict, wt_keydict, wt_keylist2, enzymes, only_one_enzyme, p)
            printed = True
    if printed:
        digestion_found = input("Did you found a fitting digestion? y/n\n")

    if not printed or digestion_found == "n":
        wt_keylist4, wt_keydict2, wt_splitdic2 = southern_two_enzymes(wt_splitdic, wt_probe_bindingsites, wt_keyfeatures)
        si_keylist4, si_keydict2, si_splitdic2 = southern_two_enzymes(si_splitdic, si_probe_bindingsites, si_keyfeatures)
        mi_keylist4, mi_keydict2, mi_splitdic2 = southern_two_enzymes(mi_splitdic, mi_probe_bindingsites, mi_keyfeatures)

        final_keylist = wt_keylist4
        for o in range(len(si_keylist4)):
            if si_keylist4[o] not in final_keylist:
                final_keylist.append(si_keylist4[o])
        for n in range(len(mi_keylist4)):
            if mi_keylist4[o] not in final_keylist:
                final_keylist.append(mi_keylist4[o])

        for k in range(len(final_keylist)):
            if final_keylist[k] in wt_keydict2 and final_keylist[k] in si_keydict2 and final_keylist[k] in mi_keydict2:
                if si_keydict2[final_keylist[k]] and mi_keydict2[final_keylist[k]] \
                        and is_size_difference_valid(si_keydict2[final_keylist[k]]) \
                        and is_size_difference_valid(mi_keydict2[final_keylist[k]]):
                    enzymes = final_keylist[k].split("+")
                    only_one_enzyme = []
                    p = "none"
                    print_results(k, mi_keydict2, si_keydict2, wt_keydict2, final_keylist, enzymes, only_one_enzyme, p)
            elif final_keylist[k] in wt_keydict2 and final_keylist[k] not in si_keydict2 and final_keylist[k] not in mi_keydict2:
                enzymes = final_keylist[k].split("+")
                for m in range(2):
                    if enzymes[m] in mi_keydict and enzymes[m] in si_keydict:
                        only_one_enzyme = [si_keydict[enzymes[m]], mi_keydict[enzymes[m]]]
                        if wt_keydict2[final_keylist[k]] \
                                and is_size_difference_valid(wt_keydict2[final_keylist[k]]) and is_size_difference_valid(only_one_enzyme[0]) and is_size_difference_valid(only_one_enzyme[1]):
                            p = "wt"
                            print_results(k, mi_keydict2, si_keydict2, wt_keydict2, final_keylist, enzymes, only_one_enzyme, p)
            elif final_keylist[k] not in wt_keydict2 and final_keylist[k] in mi_keydict2 and final_keylist[k] in si_keydict2:
                enzymes = final_keylist[k].split("+")
                for m in range(2):
                    if enzymes[m] in wt_keydict:
                        only_one_enzyme = wt_keydict[enzymes[m]]
                        if si_keydict2[final_keylist[k]] and mi_keydict2[final_keylist[k]] \
                                and is_size_difference_valid(si_keydict2[final_keylist[k]]) and is_size_difference_valid(mi_keydict2[final_keylist[k]]) and is_size_difference_valid(only_one_enzyme):
                            p = "si+mi"
                            print_results(k, mi_keydict2, si_keydict2, wt_keydict2, final_keylist, enzymes, only_one_enzyme, p)

