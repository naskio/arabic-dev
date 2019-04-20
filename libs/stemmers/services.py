from stemmers.services.alkhalil_morph_sys_stemmer.alkhalilMorphoSysStemmer import stem as alkhalil_stem

# TODO: add the other stemmers
STEMMERS = {
    'alkhalil_morph_sys': alkhalil_stem,
}


# TODO: check data encoding and fix it
def stem(data, stemmer_name):
    if not stemmer_name:
        return None
    if stemmer_name in STEMMERS:
        return STEMMERS[stemmer_name](data)
    return None
