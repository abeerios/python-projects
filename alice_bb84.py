import random
alice_key = '' # generating a key to initialize the process
for x in range(8):  
    alice_key = alice_key + str(random.randint(0,1))
print("Alice's key: ", alice_key) # alice sends a random 8-bit binary digit to be encoded as a basis

alice_basis = [] # generating a key to store + or X basis
for x in range(8):
    alice_basis.append(random.choice(['+', 'X'])) # appending each bit to be one of the two basis 
print("Alice's basis: ", alice_basis) 

alice_polarized_key = ''
for x in range(8):
    if alice_key[x] == '0' and alice_basis[x] == '+': # + basis chosen to represent either H or V.
      alice_polarized_key += 'V'
    elif alice_key[x] == '1' and alice_basis[x] == '+':
        alice_polarized_key += 'H'
for x in range(8): 
    if alice_basis[x] == 'X':
        if random.randint(0, 1) == 0:   # X basis randomly polarized as either A or D.
            alice_polarized_key += 'D'
        else:
            alice_polarized_key += 'A'
print("Alice's polarized key:", alice_polarized_key) # final polarized key
