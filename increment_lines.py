import numpy as np
import sys
import re
import math
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

lowess = sm.nonparametric.lowess

increments = np.linspace(0, 1, num=1000)

syns = []
meros = []
hypers = []
hypos = []
stems = []
holos = []
increments = []

with open("textfiles/increments.txt") as results:
    for line in results.readlines():
        try:
            line = line.replace("\n", "")
            top, bottom, syn, mero, holo, hyper, hypo, stem, none = line.split(",")
            increments.append((float(top) + float(bottom)) / 2)
            syns.append(int(syn))
            holos.append(int(holo))
            meros.append(int(mero))
            hypers.append(int(hyper))
            hypos.append(int(hypo))
            stems.append(int(stem))
        except ValueError:
            pass
 
syns = np.array(syns)

alpha = .4

'''
print syns
x = np.arange(1, len(syns) + 1, 1)
print lowess(syns, x)
#plt.scatter(x, same_stem, alpha=.4, label='Same stem', marker="h")
z = [a[1] for a in lowess(syns, x)]
line, = plt.plot(z, label='Synonyms', linestyle='-')
'''

plt.scatter(increments, stems, color="red", alpha=alpha, label="Same stems")
plt.scatter(increments, hypers, color="purple", alpha=alpha, label="Hypernyms")
plt.scatter(increments, syns, color="green", alpha=alpha, label="Synonyms")
plt.scatter(increments, hypos, color="yellow", alpha=alpha, label="Hyponyms")
plt.scatter(increments, meros, color="orange", alpha=alpha, label="Meronyms")
plt.scatter(increments, holos, color="blue", alpha=alpha, label="Holonyms")

plt.xlabel('Cosine distance')
plt.ylabel('Count')
plt.legend(loc=2)
plt.xlim(0,1)

plt.savefig('increment_lines.png', bbox_inches='tight', pad_inches=.4)