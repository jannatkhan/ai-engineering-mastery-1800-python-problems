#13. Check prime number
n = 7

if n < 2:
    print("Not Prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
#Explanation: A prime number has exactly two positive divisors: 1 and itself.