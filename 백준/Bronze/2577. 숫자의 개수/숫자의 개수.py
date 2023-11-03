A = int(input())
B = int(input())
C = int(input())
num = A*B*C
num_str = list(str(num))
for i in range(10):
    print(num_str.count(str(i)))