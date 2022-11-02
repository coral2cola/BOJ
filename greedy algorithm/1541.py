import sys
import re

data = sys.stdin.readline().rstrip()
#print(data[0])


numbers = re.findall('\d+', data)
alphas = re.findall('[+-]', data)

result = int(numbers[0])
index = 1
dominus = 0
tmp = 0

for i in range(len(alphas)):
    if alphas[i] == '+':
        if dominus == 0:
            result += int(numbers[index])
        else:
            result -= int(numbers[index])
    else: # 빼기일 경우
        result -= int(numbers[index])
        dominus = 1
    
    index += 1
    
print(result)