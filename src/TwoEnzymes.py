def checkDigestionWithTwoEnzymes(splitdic, probebindingsites, keyfeatures):
    keylist2 = []; newSplitDic = {}; keylistTwoEnzymes = []; keydict = {}; banddic = {}

    for key in splitdic:
        keylist2.append(key)

    for i in range(len(keylist2)):
        for j in range(i+1, len(keylist2)):
            bandsTwoEnzymes = splitdic[keylist2[i]]+splitdic[keylist2[j]]
            keylistTwoEnzymes.append(keylist2[i]+"+"+keylist2[j])
            bandsTwoEnzymes.sort()
            newSplitDic.update({keylist2[i]+"+"+keylist2[j]: bandsTwoEnzymes})

    for k in range(len(keylistTwoEnzymes)):
        surroundingBands = []
        for m in range(len(keyfeatures)):
            smallerBands = []; biggerBands = []
            twoEnzymes = newSplitDic[keylistTwoEnzymes[k]]
            for v in range(len(twoEnzymes)):
                if int(twoEnzymes[v]) < int(probebindingsites[keyfeatures[m]][0]):
                    smallerBands.append(twoEnzymes[v])
                if int(twoEnzymes[v]) > int(probebindingsites[keyfeatures[m]][1]):
                    biggerBands.append(twoEnzymes[v])
            if smallerBands and biggerBands:
                surroundingBands.append([smallerBands[-1], biggerBands[0]])
            else:
                surroundingBands.append([])
            banddic.update({keylistTwoEnzymes[k]: surroundingBands})

    for n in range(len(keylistTwoEnzymes)):
        keylist3 = []
        for q in range(len(keyfeatures)):
            bandsTwoEnzymes = banddic[keylistTwoEnzymes[n]]
            if bandsTwoEnzymes and bandsTwoEnzymes[q] and bandsTwoEnzymes[q][1] - bandsTwoEnzymes[q][0] not in keylist3:
                keylist3.append(bandsTwoEnzymes[q][1] - bandsTwoEnzymes[q][0])
                keylist3.sort(reverse=True)
        keydict.update({keylistTwoEnzymes[n]: keylist3})

    return keylistTwoEnzymes, keydict, newSplitDic
