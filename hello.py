import random
# Create your models here.

def get_uid(number):
    alphabet = '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    taille=len(alphabet)
    result=[]
    for i in range(1,number):
        result.append(alphabet[random.randint(0,taille-1)])
    return ''.join(result)

for i in range(1,100):
    result = get_uid(7)
    print(result)