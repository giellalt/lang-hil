"""Convert DictionaryForMIDs dictionary to lexc entries."""

import re
from zipfile import ZipFile

trans_table = [('á', 'á'),
               ('í', 'í')]

lines = []
with ZipFile('DictionaryForMIDs/DictionaryForMIDs_HilEng_KVED.jar') as zf:
    for fname in zf.namelist():
        if re.search(r'directory[0-9]+\.csv', fname):
            with zf.open(fname) as f:
                lines.extend(f.readlines())

# The list in `lines` is a list of strings

cc = 'ANV'  # TODO name the continuation class (this idea stands from AdjectiveNounVerb)
with open('dfm.lexc', 'w') as f:
    print('LEXICON DictionaryForMIDs_roots', file=f)
    for line in lines:
        line = line.decode('utf8')
        stem, gloss = line.split('\t')
        for find, replace in trans_table:
            if find in stem:
                print(find, stem)
                stem.replace(find, replace)
                assert find not in replace
        gloss = re.sub(r'\[01([^\]]+)\]', r'\1', gloss)
        gloss = re.split(r'(?<!Sp)[!,;.]|\\n', gloss)[0].strip()
        if '[01' in gloss:
            print('DEBUG', repr(line), gloss, gloss)
        gloss = gloss.replace('"', '%"')
        print(f'{stem} {cc} "{gloss}" ;', file=f)
