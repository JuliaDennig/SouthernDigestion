def getEnzymeBindingSitesDict(sequence, probebindingsites, keyfeatures):
    from Enzymdatabase import getEnzymesDicts
    import re
    JoergsEnzymes, TopEnzymes = getEnzymesDicts()

    splitdic = {}; keylist = []
    for i in range(len(TopEnzymes)):
        splitlist = []
        enzymebinding = JoergsEnzymes[TopEnzymes[i]][0].replace("^", "")
        cut = JoergsEnzymes[TopEnzymes[i]][0].find("^")
        binding = re.compile(enzymebinding)
        for j in binding.finditer(sequence):
            split = cut + j.start() + 1
            appendEnzymeBindingSites(TopEnzymes, i, keyfeatures, keylist, probebindingsites, split, splitdic, splitlist)
        if "DraIII-HF" in TopEnzymes[i]:
            binding = re.compile(r'CAC\w{3}GTG')
            for m in binding.finditer(sequence):
                split = cut + m.start() + 1
                appendEnzymeBindingSites(TopEnzymes, i, keyfeatures, keylist, probebindingsites, split, splitdic, splitlist)
        elif "XcmI" in TopEnzymes[i]:
            binding = re.compile(r'CCA\w{9}TGG')
            for m in binding.finditer(sequence):
                split = cut + m.start() + 1
                appendEnzymeBindingSites(TopEnzymes, i, keyfeatures, keylist, probebindingsites, split, splitdic, splitlist)

    for key in keylist:
        splitdic.pop(key)
    splitdic_multiple = dict(splitdic)

    for key2 in splitdic_multiple.copy():
        if len(splitdic_multiple[key2]) == 1:
            splitdic_multiple.pop(key2)
    return splitdic, splitdic_multiple


def appendEnzymeBindingSites(TopEnzymes, i, keyfeatures, keylist, probebindingsites, split, splitdic, splitlist):
    splitlist.append(split)
    splitdic.update({TopEnzymes[i]: splitlist})
    for k in range(len(probebindingsites)):
        keyfeature = probebindingsites[keyfeatures[k]]
        if (int(keyfeature[0]) <= split <= int(keyfeature[1])) and TopEnzymes[i] not in keylist:
            keylist.append(TopEnzymes[i])
            break
