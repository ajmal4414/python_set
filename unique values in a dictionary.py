#1programme to print all unique values in a dictionary

dict1=[{"V":"SOO1"},{"V":"SOO2"},{"VI":"SOO1"},{"VI":"SOO5"},{"VII":"SOO5"},{"V":"SOO9"},{"VIII":"SOO7"}]
print("Original list:",dict1)
u_value= set(val for dic in dict1 for val in dic.values())
print("unique values are:", u_value)