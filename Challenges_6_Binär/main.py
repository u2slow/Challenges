
#8 4 2 1 
#1 0 1 1

def int2bin(b):
    bi = b[2:]
    bi = bi[::-1]
    result = 0
    counter = len(bi) - 1

    while counter >= 0:
        if bi[counter ] == "1":
            result += 2**counter
        counter -=1
    return result 


print(bin(12))
print(int2bin(bin(133700)))
