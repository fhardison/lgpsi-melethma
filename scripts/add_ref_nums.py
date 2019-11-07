import os
import re


FILES = [
("00", os.path.join('..', 'src', 'grammar-index.md')),
("01", os.path.join('..', 'src', '001-exercises.md')),
("02", os.path.join('..', 'src', '002-exercises.md')),
("03", os.path.join('..', 'src', '003-exercises.md')),
("04", os.path.join('..', 'src', '004-exercises.md'))
]



for FILE in FILES:
    print(FILE[1])
    with open(FILE[1], 'r', encoding="UTF-8") as f:
        cons = []
        for line in f:
            if not(line.strip() == ''):
                cons.append(re.sub(r'\d\d\.\d+ ','',line.rstrip()))
    with open(FILE[1], 'w', encoding="UTF-8") as g:
        LCOUNT = 1
        prefix = FILE[0]
        for line in cons:
            print(f"{prefix}.{LCOUNT} {line}", file=g)
            LCOUNT += 1
