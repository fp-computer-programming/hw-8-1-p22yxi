# Yongdong Xi

def testnum(n):
    if (int(n) % 2) == 0:
        print('{0} is divisible by 2'.format(n))
    else:
        print('{0} is  not divisible by 2'.format(n))
    if (int(n) % 3) == 0:
        print('{0} is divisible by 3'.format(n))
    else:
        print('{0} is  not divisible by 3'.format(n))
    if (int(n) % 3) == 0:
            print('{0} is divisible by 3'.format(n))
    else:
        print('{0} is  not divisible by 3'.format(n))
        

num = int(input("Give me a numbe: "))
testnum(num)