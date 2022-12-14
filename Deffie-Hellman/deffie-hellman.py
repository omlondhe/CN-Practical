# Both the persons will be agreed upon the
# public keys G and P
# A prime number P is taken
P = 23

# A primitive root for P, G is taken
G = 9

print(f'The Value of P is : {P}')
print(f'The Value of G is : {G}')

# Alice will choose the private key a
a = 4
print(f'The Private Key a for Alice is : {a}')

# gets the generated key
x = int(pow(G,a,P))

# Bob will choose the private key b
b = 3
print(f'The Private Key b for Bob is : {b}')

# gets the generated key
y = int(pow(G,b,P))

# Secret key for Alice
ka = int(pow(y,a,P))

# Secret key for Bob
kb = int(pow(x,b,P))

print(f'Secret key for the Alice is : {ka}')
print(f'Secret Key for the Bob is : {kb}')
