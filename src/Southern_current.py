def southern_one_enzyme():
    from OpenApe import get_information_from_ape_file
    sequence, probebindingsites, keyfeatures = get_information_from_ape_file()

    from EnzymeBindingSites import get_enzyme_binding_sites_dict
    splitdic, splitdic_multiple = get_enzyme_binding_sites_dict(sequence, probebindingsites, keyfeatures)

    from OneEnzyme import check_digestion_with_one_enzyme
    keylist2, keydict = check_digestion_with_one_enzyme(splitdic_multiple, probebindingsites, keyfeatures)

    return keylist2, keydict, splitdic, probebindingsites, keyfeatures


def southern_two_enzymes(splitdic, probebindingsites, keyfeatures):
    from TwoEnzymes import check_digestion_with_two_enzymes
    keylist2, keydict2, splitdic2 = check_digestion_with_two_enzymes(splitdic, probebindingsites, keyfeatures)

    return keylist2, keydict2, splitdic2
