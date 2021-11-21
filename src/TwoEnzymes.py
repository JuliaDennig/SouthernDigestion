def check_digestion_with_two_enzymes(splitdic, probe_bindingsites, keyfeatures):
    keylist2 = []; new_splitdict = {}; keylist_two_enzymes = []; keydict = {}; banddict = {}

    for key in splitdic:
        keylist2.append(key)

    for i in range(len(keylist2)):
        for j in range(i+1, len(keylist2)):
            bands_two_enzymes = splitdic[keylist2[i]]+splitdic[keylist2[j]]
            keylist_two_enzymes.append(keylist2[i]+"+"+keylist2[j])
            bands_two_enzymes.sort()
            new_splitdict.update({keylist2[i]+"+"+keylist2[j]: bands_two_enzymes})

    for k in range(len(keylist_two_enzymes)):
        surrounding_bands = []
        for m in range(len(keyfeatures)):
            smaller_bands = []; bigger_bands = []
            two_enzymes = new_splitdict[keylist_two_enzymes[k]]
            for v in range(len(two_enzymes)):
                if int(two_enzymes[v]) < int(probe_bindingsites[keyfeatures[m]][0]):
                    smaller_bands.append(two_enzymes[v])
                if int(two_enzymes[v]) > int(probe_bindingsites[keyfeatures[m]][1]):
                    bigger_bands.append(two_enzymes[v])
            if smaller_bands and bigger_bands:
                surrounding_bands.append([smaller_bands[-1], bigger_bands[0]])
            else:
                surrounding_bands.append([])
            banddict.update({keylist_two_enzymes[k]: surrounding_bands})

    for n in range(len(keylist_two_enzymes)):
        keylist3 = []
        for q in range(len(keyfeatures)):
            bands_two_enzymes = banddict[keylist_two_enzymes[n]]
            if bands_two_enzymes and bands_two_enzymes[q] and bands_two_enzymes[q][1] - bands_two_enzymes[q][0] not in keylist3:
                keylist3.append(bands_two_enzymes[q][1] - bands_two_enzymes[q][0])
                keylist3.sort(reverse=True)
        keydict.update({keylist_two_enzymes[n]: keylist3})

    return keylist_two_enzymes, keydict, new_splitdict
