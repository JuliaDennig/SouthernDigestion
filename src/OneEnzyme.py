def check_digestion_with_one_enzyme(splitdic_multiple, probe_bindingsites, keyfeatures):
    keylist2, new_keylist = [], []
    keydict = {}

    for key in splitdic_multiple:
        keylist2.append(key)

    for i in range(len(keylist2)):
        bands, keylist3, new_keylist = [], [], []
        for j in range(len(splitdic_multiple[keylist2[i]])):
            bands.append(splitdic_multiple[keylist2[i]][j])
        bands.sort()
        banddict = {}
        for k in range(len(keyfeatures)):
            smaller_bands, bigger_bands, surrounding_bands = [], [], []
            for v in range(len(bands)):
                if int(bands[v]) < int(probe_bindingsites[keyfeatures[k]][0]):
                    smaller_bands.append(bands[v])
                if int(bands[v]) > int(probe_bindingsites[keyfeatures[k]][1]):
                    bigger_bands.append(bands[v])
            if smaller_bands != [] and bigger_bands != []:
                surrounding_bands.append(smaller_bands[-1])
                surrounding_bands.append(bigger_bands[0])
            banddict.update({keyfeatures[k]: surrounding_bands})

        for l in range(len(keyfeatures)):
            current_bands = banddict[keyfeatures[l]]
            if current_bands and current_bands[1] - current_bands[0] not in keylist3:
                keylist3.append(current_bands[1] - current_bands[0])
                keylist3.sort(reverse=True)
            else:
                break

        if keylist3:
            keydict.update({keylist2[i]: keylist3})

    for m in range(len(keylist2)):
        if keylist2[m] in keydict:
            new_keylist.append(keylist2[m])

    return new_keylist, keydict
