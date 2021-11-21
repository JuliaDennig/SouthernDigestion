from OpenApe import get_information_from_ape_file
from EnzymeBindingSites import get_enzyme_binding_sites_dict
from OneEnzyme import check_digestion_with_one_enzyme
from TwoEnzymes import check_digestion_with_two_enzymes

def southern_one_enzyme():
    sequence, probebindingsites, keyfeatures = get_information_from_ape_file()

    splitdic, splitdic_multiple = get_enzyme_binding_sites_dict(sequence, probebindingsites, keyfeatures)

    keylist2, keydict = check_digestion_with_one_enzyme(splitdic_multiple, probebindingsites, keyfeatures)

    return keylist2, keydict, splitdic, probebindingsites, keyfeatures


def southern_two_enzymes(splitdic, probebindingsites, keyfeatures):
    keylist2, keydict2, splitdic2 = check_digestion_with_two_enzymes(splitdic, probebindingsites, keyfeatures)

    return keylist2, keydict2, splitdic2
