"""Convert DictionaryForMIDs dictionary to lexc entries."""

from collections import defaultdict
import re
from zipfile import ZipFile

trans_table = [('á', 'a\u0301'),
               ('à$', 'a<K>'),
               ('à(?=[^aeiouáàâéèêíìîóòôúùû-])', 'a-'),
               ('à(?=[aeiouáàâéèêíìîóòôúùû-])', 'a'),
               ('â(?=[^aeiouáàâéèêíìîóòôúùû-]|$)', 'a\u0301<K>'),
               ('â(?=[aeiouáàâéèêíìîóòôúùû-])', 'a\u0301'),
               ('é', 'e\u0301'),
               ('è$', 'e<K>'),
               ('è(?=[^aeiouáàâéèêíìîóòôúùû-])', 'e-'),
               ('è(?=[aeiouáàâéèêíìîóòôúùû-])', 'e'),
               ('ê(?=[^aeiouáàâéèêíìîóòôúùû-]|$)', 'e\u0301<K>'),
               ('ê(?=[aeiouáàâéèêíìîóòôúùû-])', 'e\u0301'),
               ('í', 'i\u0301'),
               ('ì$', 'i<K>'),
               ('ì(?=[^aeiouáàâéèêíìîóòôúùû-])', 'i-'),
               ('ì(?=[aeiouáàâéèêíìîóòôúùû-])', 'i'),
               ('î(?=[^aeiouáàâéèêíìîóòôúùû-]|$)', 'i\u0301<K>'),
               ('î(?=[aeiouáàâéèêíìîóòôúùû-])', 'i\u0301'),
               ('ó', 'o\u0301'),
               ('ò$', 'o<K>'),
               ('ò(?=[^aeiouáàâéèêíìîóòôúùû-])', 'o-'),
               ('ò(?=[aeiouáàâéèêíìîóòôúùû-])', 'o'),
               ('ô(?=[^aeiouáàâéèêíìîóòôúùû-]|$)', 'o\u0301<K>'),
               ('ô(?=[aeiouáàâéèêíìîóòôúùû-])', 'o\u0301'),
               ('ú', 'u\u0301'),
               ('ù$', 'u<K>'),
               ('ù(?=[^aeiouáàâéèêíìîóòôúùû-])', 'u-'),
               ('ù(?=[aeiouáàâéèêíìîóòôúùû-])', 'u'),
               ('û(?=[^aeiouáàâéèêíìîóòôúùû-]|$)', 'u\u0301<K>'),
               ('û(?=[aeiouáàâéèêíìîóòôúùû-])', 'u\u0301')]

lines = []
with ZipFile('DictionaryForMIDs/DictionaryForMIDs_HilEng_KVED.jar') as zf:
    for fname in zf.namelist():
        if re.search(r'directory[0-9]+\.csv', fname):
            with zf.open(fname) as f:
                lines.extend(f.readlines())

# The list in `lines` is a list of strings

cc = 'ANV'  # TODO name the continuation class (this idea stands from AdjectiveNounVerb)
with open('content.lexd', 'w') as f:
    print('LEXICON Stem(4)', file=f)
    flag_dict = defaultdict(list)
    for line in lines:
        line = line.decode('utf8')
        stem, gloss = line.split('\t')
        new_stem = stem.split(',')[0]
        if new_stem.startswith('-'):
            continue
        for find, replace in trans_table:
            if re.search(find, new_stem):
                #print(find, replace, stem)
                new_stem = re.sub(find, replace, new_stem)
                assert not re.search(find, new_stem)
        try:
            c = '(?:ng|[-bcdfghjklmnpqrstvwxyz])'
            v = '(?:[aeiou]\u0301?)'
            #                                  s1    s2  s3                s4            s5
            s1, s2, s3, s4, s5 = re.match(fr'({c}*)({v})({c}*(?:<K>)?{v}?)({c}*(?:<K>)?)([-\u0301a-z]*(?:<K>)?)$', new_stem, flags=re.I).groups()
            if not s1:
                s1 = ':'
            if not s2:
                raise ValueError(stem)
            if not s3:
                s3 = ':'
            if re.match(r'[aeiou]', s5):
                s5 = s4 + s5
            else:
                s3 = s3 + s4
            if not s5:
                s5 = ':'
        except AttributeError:
            print(new_stem)
            continue
        gloss = re.sub(r'\[01([^\]]+)\]', r'\1', gloss)
        gloss = re.split(r'(?<!Sp)[!,;.]|\\n', gloss)[0].strip()
        if '[01' in gloss:
            print('DEBUG', repr(line), gloss, gloss)
        gloss = gloss.replace('"', '%"')
        print(f'{s1} {s2} {s3} {s5} # {gloss} !{{{stem}}}', file=f)
