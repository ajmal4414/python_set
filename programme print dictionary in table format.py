#4.programme print dictionary in table format

dict1={'c1':[12],'c2':[20],'c3':[18]}

for row in zip(* ([key] +(value) for key, value in sorted(dict1.items()))):
    print(* row)