def southernOneEnzyme():
    from OpenApe import getInformationFromApeFile
    sequence, probebindingsites, keyfeatures = getInformationFromApeFile()

    from EnzymeBindingSites import getEnzymeBindingSitesDict
    splitdic, splitdic_multiple = getEnzymeBindingSitesDict(sequence, probebindingsites, keyfeatures)

    from OneEnzyme import checkDigestionWithOneEnzyme
    keylist2, keydict = checkDigestionWithOneEnzyme(splitdic_multiple, probebindingsites, keyfeatures)

    return keylist2, keydict, splitdic, probebindingsites, keyfeatures


def southernTwoEnzymes(splitdic, probebindingsites, keyfeatures):
    from TwoEnzymes import checkDigestionWithTwoEnzymes
    keylist2, keydict2, splitdic2 = checkDigestionWithTwoEnzymes(splitdic, probebindingsites, keyfeatures)

    return keylist2, keydict2, splitdic2
