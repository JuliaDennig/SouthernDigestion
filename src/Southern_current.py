from OpenApe import get_location_of_ape_file
from OpenApe import get_information_from_ape_file
from EnzymeBindingSites import get_enzyme_binding_sites_dict
from OneEnzyme import check_digestion_with_one_enzyme
from TwoEnzymes import check_digestion_with_two_enzymes

def southern_one_enzyme():
    # runs OpenApe.py, EnzymeBindingSites.py and OneEnzyme.py

    apelines = get_location_of_ape_file()

    sequence, probe_bindingsites, keyfeatures = get_information_from_ape_file(apelines)

    splitdic, splitdic_multiple = get_enzyme_binding_sites_dict(sequence, probe_bindingsites, keyfeatures)

    keylist2, keydict = check_digestion_with_one_enzyme(splitdic_multiple, probe_bindingsites, keyfeatures)

    return keylist2, keydict, splitdic, probe_bindingsites, keyfeatures


def southern_two_enzymes(splitdict, probe_bindingsites, keyfeatures):
    # takes splitdict, probe_bindingsites and keyfeatures frome southern_one_enzyme and runs TwoEnzymes.py

    keylist2, keydict2, splitdic2 = check_digestion_with_two_enzymes(splitdict, probe_bindingsites, keyfeatures)

    return keylist2, keydict2, splitdic2
