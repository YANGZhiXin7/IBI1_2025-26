a = 5.08 # The population of Scottish population in 2004
b = 5.33 # The population of Scottish population in 2014
c = 5.55 # The population of Scottish population in 2024
d = b-c # The change between 2004 and 2014
e = c-b # The change between 2014 and 2024
if d == e:
    print("e=d") # check if d=e
if d > e:
    print("d > e")
else:
    print("d < e") # check if d>e or d<e The out come is d < e
f = d//a
g = e//b
if f > g:
    print("The change between 2004 and 2014 is larger than the change between 2014 and 2024.")
else:
    print("The change between 2014 and 2024 is larger than the change between 2004 and 2014.")
# The change between 2014 and 2024 is larger than the change between 2004 and 2014.
# And the change rate between 2014 and 2024 is lager than the change rate between 2004 and 2014

X = True
Y = False
W = X or Y
print(W) # Outcome: True

A = True
B = True
C = A or B
print(C) # Outcome: True

G = False
H = True
I = G or H
print(I) # Outcome: False

D = False
E = False
F = D or E
print(F) # Outcome: False

# So The truth table should be that:
# X        Y       X or Y (W)
# True.   Flase.      True. 
# True.   True.       Ture. 
# False   True.       True
# False   False.      False