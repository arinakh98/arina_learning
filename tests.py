#цикл while
#loop = 0
#while loop < 10:
    #print(f"Номер круга {loop}")
    #loop = loop + 1#


import random

loop = 0
while loop < 10:
    print(f"Номер круга {loop}")
    loop = loop + 1
    if random.randint(1, 5) == 4:
        break
        
