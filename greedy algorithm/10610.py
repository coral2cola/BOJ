# 양수 N
# 30의 배수가 되는 가장 큰 수 ..... 숫자 섞어서.
# 배수판정법 : 각 자리수 전부 더해서 3배수면 3의 배수임
# 배수판정법 : 끝이 0으로 끝나면 10의 배수임

# 조건만 만족하면 맨 끝에 0 넣고 큰 숫자 순서대로 배열

n = int(input())

list = []
for i in str(n):
    list.append(i)
    
list.sort()

if list[0] != '0':
    print(-1)
else:
    sum = 0
    for i in range(len(list)):
        sum += int(list[i])
    
    if sum % 3 != 0:
        print(-1)
    else:
        a = ''
        i = len(list)
        while i > 0:
            a += list[i-1]
            i -= 1
        
        print(a)

