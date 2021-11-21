import Enzymdatabase
from Southern_current import southern_one_enzyme
from Southern_current import southern_two_enzymes
from BiologicalCheck import is_size_difference_valid

def print_results(index, mut_keydict, wt_keydict, keyList, enzymes, only_one_enzyme, p):
    # prints the results of the in silico Southern digestion:
    # enzyme(s) to use, resulting band(s) for wildtype/mutation, binding site(s),
    # cutting type(s), buffer, and  temperature

    MYENZYMES = Enzymdatabase.MYENZYMES
    if not enzymes:
        print(keyList[index])
    else:
        print(enzymes[0], "+", enzymes[1])

    if not only_one_enzyme:
        print("resulting bands for wildtype", wt_keydict[keyList[index]])
        print("resulting bands for mutation", mut_keydict[keyList[index]])
    elif p == "wt":
        print("resulting bands for wildtype", wt_keydict[keyList[index]])
        print("resulting bands for mutation", only_one_enzyme)
    elif p == "mut":
        print("resulting bands for wildtype", only_one_enzyme)
        print("resulting bands for mutation", mut_keydict[keyList[index]])

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

def southern_in_locus():
    # runs OneEnzyme.py and BiologicalCheck.py for wildtype and mutation

    print("WILDTYPE")
    wt_keylist2, wt_keydict, wt_splitdic, wt_probe_bindingsites, wt_keyfeatures = southern_one_enzyme()
    print("MUTATION")
    mut_keylist2, mut_keydict, mut_splitdic, mut_probe_bindingsites, mut_keyfeatures = southern_one_enzyme()

    print("\nRESULT")

    printed = False
    for i in range(len(wt_keylist2)):
        if wt_keylist2[i] in wt_keydict and wt_keylist2[i] in mut_keydict and mut_keydict[wt_keylist2[i]] \
                and is_size_difference_valid(wt_keydict[wt_keylist2[i]]) and is_size_difference_valid(mut_keydict[wt_keylist2[i]]) \
                and (len(wt_keydict[wt_keylist2[i]]) == len(mut_keydict[wt_keylist2[i]]) > 1 or len(mut_keydict[wt_keylist2[i]]) != len(wt_keydict[wt_keylist2[i]])):
            enzymes, only_one_enzyme = [], []
            p = "none"
            print_results(i, mut_keydict, wt_keydict, wt_keylist2, enzymes, only_one_enzyme, p)
            printed = True
    if printed:
        digestion_found = input("Did you found a fitting digestion? y/n\n")

    if not printed or digestion_found == "n":
        wt_keylist4, wt_keydict2, wt_splitdic2 = southern_two_enzymes(wt_splitdic, wt_probe_bindingsites, wt_keyfeatures)
        mut_keylist4, mut_keydict2, mut_splitdic2 = southern_two_enzymes(mut_splitdic, mut_probe_bindingsites, mut_keyfeatures)

        final_keylist = wt_keylist4
        for k in range(len(mut_keylist4)):
            if mut_keylist4[k] not in final_keylist:
                final_keylist.append(mut_keylist4[k])
        final_keylist.sort()

        for j in range(len(final_keylist)):
            if final_keylist[j] in wt_keydict2 and final_keylist[j] in mut_keydict2:
                if wt_keydict2[final_keylist[j]] and mut_keydict2[final_keylist[j]] \
                        and is_size_difference_valid(wt_keydict2[final_keylist[j]]) and is_size_difference_valid(mut_keydict2[final_keylist[j]]) \
                        and (len(wt_keydict2[final_keylist[j]]) == len(mut_keydict2[final_keylist[j]]) > 1 or len(wt_keydict2[final_keylist[j]]) != len(mut_keydict2[final_keylist[j]])):
                    enzymes = final_keylist[j].split("+")
                    only_one_enzyme = []
                    p = "none"
                    print_results(j, mut_keydict2, wt_keydict2, final_keylist, enzymes, only_one_enzyme, p)
            elif final_keylist[j] in wt_keydict2 and final_keylist[j] not in mut_keydict2:
                enzymes = final_keylist[j].split("+")
                for m in range(2):
                    if enzymes[m] in mut_keydict:
                        only_one_enzyme = mut_keydict[enzymes[m]]
                        if wt_keydict2[final_keylist[j]] \
                                and is_size_difference_valid(wt_keydict2[final_keylist[j]]) and is_size_difference_valid(only_one_enzyme) \
                                and (len(wt_keydict2[final_keylist[j]]) == len(only_one_enzyme) > 1 or len(wt_keydict2[final_keylist[j]]) != len(only_one_enzyme)):
                            p = "wt"
                            print_results(j, mut_keydict2, wt_keydict2, final_keylist, enzymes, only_one_enzyme, p)
            elif final_keylist[j] not in wt_keydict2 and final_keylist[j] in mut_keydict2:
                enzymes = final_keylist[j].split("+")
                for m in range(2):
                    if enzymes[m] in wt_keydict:
                        only_one_enzyme = wt_keydict[enzymes[m]]
                        if mut_keydict2[final_keylist[j]] \
                                and is_size_difference_valid(mut_keydict2[final_keylist[j]]) and is_size_difference_valid(only_one_enzyme) \
                                and (len(mut_keydict2[final_keylist[j]]) == len(only_one_enzyme) > 1 or len(mut_keydict2[final_keylist[j]]) != len(only_one_enzyme)):
                            p = "mut"
                            print_results(j, mut_keydict2, wt_keydict2, final_keylist, enzymes, only_one_enzyme, p)

