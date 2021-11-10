def getInformationFromApeFile():
    apelines = []; features = []; keyfeatures = []; yes = ["yes", "y", "Y", "Yes"]; no = ["no", "n", "No", "N"]
    apefile = input("Where is the apefile saved? ")
    with open(apefile, "r") as apefile:
        apelines.append(apefile.readlines())
    for i, elem in enumerate(apelines[0]):
        if 'linear' in elem:
            print("\nThe sequence is linear.\n")
        elif 'circular' in elem:
            print("The sequence is circular.\n")

    sequencestart = apelines[0].index("ORIGIN\n") + 1
    sequence = ''.join(apelines[0][sequencestart:])
    sequence = sequence.replace("\n", "").replace(" ", "").replace("\t", "").replace("/", "").upper()
    for j in range(0, 10):
        sequence = sequence.replace(str(j), "")

    featurestart = apelines[0].index("FEATURES             Location/Qualifiers\n") + 1
    for k in range(featurestart, sequencestart-1):
        features.append(apelines[0][k])

    probes = []; labels = []
    for l, elem in enumerate(features):
        if '..' in elem:
            probes.append(l)
        if '/label=' in elem:
            labels.append(l)

    probesdic = {}; labellist = []
    import re
    for m in range(0, len(probes)):
        bindingsite = re.sub('\D', ' ', features[probes[m]])
        bindingsites = bindingsite.split(" ")
        bindingsites = list(filter(None, bindingsites))
        label = features[labels[m]].replace("/label=", "").replace("\n", "").replace(" ", "").replace('"', "")
        labellist.append(label)
        probesdic.update({label: bindingsites})
    probebindingsites = {}

    print("Following features are marked in the sequence: ", labellist)

    chooseProbeBinding(keyfeatures, probebindingsites, probesdic)

    while True:
        askagain = input("Is there another feature where the probe binds? y/n\n")
        if askagain in yes:
            chooseProbeBinding(keyfeatures, probebindingsites, probesdic)
        elif askagain in no:
            break
    return sequence, probebindingsites, keyfeatures


def chooseProbeBinding(keyfeatures, probebindingsites, probesdic):
    while True:
        probebindingsite = input("Please choose the features where the probe is binding.\n")
        if probebindingsite in probesdic and probebindingsite not in probebindingsites:
            probebindingsites.update({probebindingsite: probesdic[probebindingsite]})
            keyfeatures.append(probebindingsite)
            break
