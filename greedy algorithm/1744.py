n  = int(input())

plus = []
minus = []
for i in range(n):
    a = int(input())
    if a > 0:
        plus.append(a)
    else:
        minus.append(a)


plus.sort() # [ 1, 2, 3, ...]
minus.sort() # [..., -3, -2, -1, 0 ]

result = 0

# 양수 먼저 구하기
num = len(plus)
while num > 0:
    if num == 1:
        result += plus[0]
        break
    
    big = plus[num-1]
    small = plus[num-2]
    
    # 1*2 < 1+2, 1*3 < 1+3 이므로 예외처리
    if small == 1:
        result += big
        result += small
    else:
        result += big*small
    num -= 2

i = 0
while i < len(minus):
    if i == len(minus)-1:
        result += minus[i]
        break
    
    small = minus[i]
    big = minus[i+1]
    
    result += small*big
    i += 2

print(result)