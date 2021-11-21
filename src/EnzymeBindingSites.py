import Enzymdatabase
import re

def append_enzyme_binding_sites(TopEnzymes, i, keyfeatures, keylist, probe_bindingsites, split, splitdic, splitlist):
    splitlist.append(split)
    splitdic.update({TopEnzymes[i]: splitlist})
    for k in range(len(probe_bindingsites)):
        keyfeature = probe_bindingsites[keyfeatures[k]]
        if (int(keyfeature[0]) <= split <= int(keyfeature[1])) and TopEnzymes[i] not in keylist:
            keylist.append(TopEnzymes[i])
            break

def get_enzyme_binding_sites_dict(sequence, probe_bindingsites, keyfeatures):
    MYENZYMES = Enzymdatabase.MYENZYMES
    TOPENZYMES = Enzymdatabase.TOPENZYMES

    splitdic = {}
    keylist = []
    for i in range(len(TOPENZYMES)):
        splitlist = []
        enzyme_binding = MYENZYMES[TOPENZYMES[i]][0].replace("^", "")
        cut = MYENZYMES[TOPENZYMES[i]][0].find("^")
        binding = re.compile(enzyme_binding)
        for j in binding.finditer(sequence):
            split = cut + j.start() + 1
            append_enzyme_binding_sites(TOPENZYMES, i, keyfeatures, keylist, probe_bindingsites, split, splitdic, splitlist)
        if "DraIII-HF" in TOPENZYMES[i]:
            binding = re.compile(r'CAC\w{3}GTG')
            for m in binding.finditer(sequence):
                split = cut + m.start() + 1
                append_enzyme_binding_sites(TOPENZYMES, i, keyfeatures, keylist, probe_bindingsites, split, splitdic, splitlist)
        elif "XcmI" in TOPENZYMES[i]:
            binding = re.compile(r'CCA\w{9}TGG')
            for m in binding.finditer(sequence):
                split = cut + m.start() + 1
                append_enzyme_binding_sites(TOPENZYMES, i, keyfeatures, keylist, probe_bindingsites, split, splitdic, splitlist)

    for key in keylist:
        splitdic.pop(key)
    splitdic_multiple = dict(splitdic)

    for key2 in splitdic_multiple.copy():
        if len(splitdic_multiple[key2]) == 1:
            splitdic_multiple.pop(key2)
    return splitdic, splitdic_multiple

