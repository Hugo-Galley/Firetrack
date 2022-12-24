import hashlib

password = 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'

#passs = input("entre mdp ")

#if hashlib.sha256(passs.encode('utf-8')).hexdigest() == password:
    #print('rEusie')
#else:
    #print("Cest nul")
print(hashlib.sha256(b'Admin').hexdigest())