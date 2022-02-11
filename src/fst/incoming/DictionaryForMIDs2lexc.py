"""Convert DictionaryForMIDs dictionary to lexc entries."""

import re
from zipfile import ZipFile

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
        # TODO add logic here to parse each line
        stem = ''
        gloss = ''
        print(f'{stem} {cc} "{gloss}" ;', file=f)
