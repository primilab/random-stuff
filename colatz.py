import random
import time


start_time = time.time()

def collatz(n):
    if(n % 2 == 0):
        return (n // 2)
    elif(n % 2 != 0):
        return (3 * n + 1)
    else:
        pass


# i = input("Input a number, any integer and you'll get 1 (eventually :) ): ")


i = 9223372036854775807 * 922337203685807



x = collatz(int(i))


if x != 1:
    while x != 1:
        x = collatz(int(x))
        print(x)
else:
    print(x)




print("--- %s seconds ---" % (time.time() - start_time))