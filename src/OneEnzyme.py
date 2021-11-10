def checkDigestionWithOneEnzyme(splitdic_multiple, probebindingsites, keyfeatures):
    keylist2 = []; keydict = {}; newKeylist = []

    for key in splitdic_multiple:
        keylist2.append(key)

    for i in range(len(keylist2)):
        bands = []; keylist3 = []; newKeylist = []
        for j in range(len(splitdic_multiple[keylist2[i]])):
            bands.append(splitdic_multiple[keylist2[i]][j])
        bands.sort()
        banddic = {}
        for k in range(len(keyfeatures)):
            smallerBands = []; biggerBands = []; surroundingBands = []
            for v in range(len(bands)):
                if int(bands[v]) < int(probebindingsites[keyfeatures[k]][0]):
                    smallerBands.append(bands[v])
                if int(bands[v]) > int(probebindingsites[keyfeatures[k]][1]):
                    biggerBands.append(bands[v])
            if smallerBands != [] and biggerBands != []:
                surroundingBands.append(smallerBands[-1])
                surroundingBands.append(biggerBands[0])
            banddic.update({keyfeatures[k]: surroundingBands})

        for l in range(len(keyfeatures)):
            currentBands = banddic[keyfeatures[l]]
            if currentBands and currentBands[1] - currentBands[0] not in keylist3:
                keylist3.append(currentBands[1] - currentBands[0])
                keylist3.sort(reverse=True)
            else:
                break

        if keylist3:
            keydict.update({keylist2[i]: keylist3})

    for m in range(len(keylist2)):
        if keylist2[m] in keydict:
            newKeylist.append(keylist2[m])

    return newKeylist, keydict
