import re


def choose_probe_binding(keyfeatures, probe_bindingsites, probesdic):
    # takes the feature(s) where the probe is binding as input

    while True:
        probe_bindingsite = input("Please choose the features where the probe is binding.\n")
        if probe_bindingsite in probesdic and probe_bindingsite not in probe_bindingsites:
            probe_bindingsites.update({probe_bindingsite: probesdic[probe_bindingsite]})
            keyfeatures.append(probe_bindingsite)
            break


def get_location_of_ape_file():
    # takes location of the ape file as input, reads the ape file one line at a time
    # and prints the type of the sequence (linear/circular)
    # returns list (apelines) with the lines from the ape file

    apelines = []
    location_apefile = input("Where is the location_apefile saved? ")
    with open(location_apefile, "r") as location_apefile:
        apelines.append(location_apefile.readlines())
    for i, elem in enumerate(apelines[0]):
        if 'linear' in elem:
            print("\nThe sequence is linear.\n")
        elif 'circular' in elem:
            print("The sequence is circular.\n")
    return apelines


def get_information_from_ape_file(apelines):
    # takes the list with the lines from the ape files, saves the sequence in a string (sequence)
    # and the features in a list (features)
    # returns sequence, list of feature where the probe is binding and dictionary with name of the feature
    # where the probe is binding as key and list of the beginning and the end of the feature as value

    features, keyfeatures = [], []
    yes = ["yes", "y", "Y", "Yes"]
    no = ["no", "n", "No", "N"]
    sequence_start = apelines[0].index("ORIGIN\n") + 1
    sequence = ''.join(apelines[0][sequence_start:])
    sequence = sequence.replace("\n", "").replace(" ", "").replace("\t", "").replace("/", "").upper()
    for j in range(0, 10):
        sequence = sequence.replace(str(j), "")

    feature_start = apelines[0].index("FEATURES             Location/Qualifiers\n") + 1
    for k in range(feature_start, sequence_start-1):
        features.append(apelines[0][k])

    probes, labels = [], []
    for o, elem in enumerate(features):
        if '..' in elem:
            probes.append(o)
        if '/label=' in elem:
            labels.append(o)

    probesdict = {}
    labellist = []
    for m in range(0, len(probes)):
        bindingsite = re.sub('\D', ' ', features[probes[m]])
        bindingsites = bindingsite.split(" ")
        bindingsites = list(filter(None, bindingsites))
        label = features[labels[m]].replace("/label=", "").replace("\n", "").replace(" ", "").replace('"', "")
        labellist.append(label)
        probesdict.update({label: bindingsites})
    probe_bindingsites = {}

    print("Following features are marked in the sequence: ", labellist)

    choose_probe_binding(keyfeatures, probe_bindingsites, probesdict)

    while True:
        ask_again = input("Is there another feature where the probe binds? y/n\n")
        if ask_again in yes:
            choose_probe_binding(keyfeatures, probe_bindingsites, probesdict)
        elif ask_again in no:
            break

    return sequence, probe_bindingsites, keyfeatures
