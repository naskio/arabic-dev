from .services.alkhalil_morph_sys_stemmer import alkhalilMorphoSysStemmer
from .services.arabic_processing_cog_stemmer import arabicProcessingCogStemmer
from .services.arabic_stemming_toolkit.ast_algo1.arabicStemmingToolkitAlgo1 import \
    ArabicStemmingToolkitStemmerAlgo1 as ast_algo1_stemmer
from .services.arabic_stemming_toolkit.ast_algo2.arabicStemmingToolkitAlgo2 import \
    ArabicStemmingToolkitStemmerAlgo2 as ast_algo2_stemmer
from .services.arabic_stemming_toolkit.ast_algo3.arabicStemmingToolkitAlgo3 import \
    ArabicStemmingToolkitStemmerAlgo3 as ast_algo3_stemmer
from .services.farasa_stemmer.farasaStemmer import FarasaStemmer as farasa_stemmer_
from .services.assems_arabic_light_stemmer import assemsArabicLightStemmer
from .services.ntlk_stemmer import ntlkIsriStemmer
from .services.qutuf_stemmer import qutufStemmer
from .services.shereen_khoja_stemmer.shereenKhojaStemmer import \
    ShereenKhojaStemmer as shereen_khoja_stemmer_
from .services.tashaphyne_stemmer import tashaphyneStemmer

from .services.lucene_arabic_analyzer.luceneArabicAnalyzerStemmer import \
    LuceneArabicAnalyzerStemmer as lucene_arabic_analyzer_stemmer_


def alkhalil_morpho_sys_stemmer(string):
    return alkhalilMorphoSysStemmer.stem(string)


def arabic_processing_cog_stemmer(string):
    return arabicProcessingCogStemmer.stem(string)


def ast1(string):
    return ast_algo1_stemmer.stem(ast_algo1_stemmer, string)


def ast2(string):
    return ast_algo2_stemmer.stem(ast_algo2_stemmer, string)


def ast3(string):
    return ast_algo3_stemmer.stem(ast_algo3_stemmer, string)


def assems_arabic_light_stemmer(string):
    return assemsArabicLightStemmer.stem(string.encode().decode())


def farasa_stemmer(string):
    return farasa_stemmer_.stem(farasa_stemmer_, string.encode().decode())


def lucene_arabic_analyzer_stemmer(string):
    return lucene_arabic_analyzer_stemmer_.stem(lucene_arabic_analyzer_stemmer_, string.encode().decode())


def ntlk_stemmer(string):
    return ntlkIsriStemmer.stem(string.encode().decode())


def qutuf_stemmer(string):
    return qutufStemmer.stem(string)


def shereen_khoja_stemmer(string):
    return shereen_khoja_stemmer_.stem(shereen_khoja_stemmer_, string)


def tashaphyne_stemmer(string):
    return tashaphyneStemmer.stem(string.encode().decode())


# TODO: add the other stemmers
STEMMERS = {
    'alkhalil_morph_sys': alkhalil_morpho_sys_stemmer,
    'arabic_processing_cog': arabic_processing_cog_stemmer,
    'Arabic_stemming_toolkit_v1': ast1,
    'Arabic_stemming_toolkit_v2': ast2,
    'Arabic_stemming_toolkit_v3': ast3,
    'farasa': farasa_stemmer,
    'arabic_light_stemmer': assems_arabic_light_stemmer,
    'ntlk_stemmer': ntlk_stemmer,
    'qutuf_stemmer': qutuf_stemmer,
    'shereen_khoja_stemmer': shereen_khoja_stemmer,
    'tashaphyne_stemmer': tashaphyne_stemmer,
    'lucene_arabic_analyzer': lucene_arabic_analyzer_stemmer,
}


def stem(string, stemmer_name=None):
    if not stemmer_name:
        return None
    if stemmer_name in STEMMERS:
        return STEMMERS[stemmer_name](string)
    return None
