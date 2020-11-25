a = int(input())
b = int(input())
a_1 = a // 1000
b_1 = a // 100 % 10
while (((a_1 * 10 + b_1) * 10 + b_1) * 10 + a_1) <= b:
    print(a_1, b_1, b_1, a_1, sep="")
    b_1 = b_1 + 1
    if ( b_1 > 9):
        a_1 = a_1 + 1
        b_1 = 0
        