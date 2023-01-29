#1.python set operations
#union method
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a.union(b)

print("the union is", c)

#intersection method
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a.intersection(b)
print("the intersection is",c)

#difference method

a={1,2,3,4,5}
b={4,5,6,7,8}
c=a.difference(b)
print("the difference is",c)

#symmetric difference

a={1,2,3,4,5}
b={4,5,6,7,8}
c=a.symmetric_difference(b)
print("symmetric difference is", c)