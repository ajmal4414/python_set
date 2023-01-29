#2.programme cobine values in python list of dictionaries

from collections import Counter
dict1=[{'item':'item1', 'amount': 400},{'item':'item2','amount': 300}, {'item':'item1','amount': 750}]
re=Counter()
for d in dict1:
    re[d['item']] +=d['amount']
print(re)