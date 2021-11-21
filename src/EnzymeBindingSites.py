import Enzymdatabase
import re


def append_enzyme_binding_sites(topenzymes, i, keyfeatures, keylist, probe_bindingsites, split, splitdict, splitlist):
    # creates dictionary with all enzymes that could cut the sequence alone (splitdict)
    # resulting in a band in Southern Blot

    splitlist.append(split)
    splitdict.update({topenzymes[i]: splitlist})
    for k in range(len(probe_bindingsites)):
        keyfeature = probe_bindingsites[keyfeatures[k]]
        if (int(keyfeature[0]) <= split <= int(keyfeature[1])) and topenzymes[i] not in keylist:
            keylist.append(topenzymes[i])
            break


def get_enzyme_binding_sites_dict(sequence, probe_bindingsites, keyfeatures):
    # checks where the enzymes in topenzymes binds in the sequence
    # returns dictionary with all enzymes that could cut the sequence alone (splitdict)
    # and a dictionary with all enzymes that need another enzyme for Southern digestion (splitdict_multiple)

    myenzymes = Enzymdatabase.MYENZYMES
    topenzymes = Enzymdatabase.TOPENZYMES

    splitdict = {}
    keylist = []
    for i in range(len(topenzymes)):
        splitlist = []
        enzyme_binding = myenzymes[topenzymes[i]][0].replace("^", "")
        cut = myenzymes[topenzymes[i]][0].find("^")
        binding = re.compile(enzyme_binding)
        for j in binding.finditer(sequence):
            split = cut + j.start() + 1
            append_enzyme_binding_sites(topenzymes, i, keyfeatures, keylist, probe_bindingsites, split, splitdict, splitlist)
        if "DraIII-HF" in topenzymes[i]:
            binding = re.compile(r'CAC\w{3}GTG')
            for m in binding.finditer(sequence):
                split = cut + m.start() + 1
                append_enzyme_binding_sites(topenzymes, i, keyfeatures, keylist, probe_bindingsites, split, splitdict, splitlist)
        elif "XcmI" in topenzymes[i]:
            binding = re.compile(r'CCA\w{9}TGG')
            for m in binding.finditer(sequence):
                split = cut + m.start() + 1
                append_enzyme_binding_sites(topenzymes, i, keyfeatures, keylist, probe_bindingsites, split, splitdict, splitlist)

    for key in keylist:
        splitdict.pop(key)
    splitdict_multiple = dict(splitdict)

    for key2 in splitdict_multiple.copy():
        if len(splitdict_multiple[key2]) == 1:
            splitdict_multiple.pop(key2)
    return splitdict, splitdict_multiple
