import sys
import re

if len(sys.argv) < 2:
    print("Insufficient arguments")
    exit()

infile = sys.argv[1]

def filter_punc(instr):
    return re.sub(r'[;\-.–,\'!#’]', '', instr)

def get_words(raw):
    return sorted(set(filter(lambda x: x.strip(), re.split(r'\b', filter_punc(raw)))))



cons = None
with open(infile, 'r', encoding="UTF-8") as f:
    cons = f.read()

newcons = get_words(cons)

with open(re.sub(r'\.\S+', '-wordlist.txt', infile ), 'w', encoding="UTF-8") as f:
    out = "\n".join(newcons)
    print(out)
    print("Total forms: " + str(len(newcons)))
    f.write("Total forms: " + str(len(newcons)))
    f.write(out)
print("DONE!")
