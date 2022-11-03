# N 명의 여학생과 M 명의 남학생 2+1
# K명은 인턴십 참여로 대회참가 못함

# 최대한 많은 팀을 만들자

# 여자쪽에서 k 명 최대한 빼는게 이득 ?
# 여자 먼저 .. 

n, m, k = map(int, input().split())

n_max = n // 2

# 만들 수 있는 팀의 최대 개수
max = min(n_max, m)

# 남는 사람 수 계산
n_left = n - (max*2)
m_left = m - max

result = max

while k > 0:
    if n_left > 0:
        n_left -= 1
        k -= 1
    elif m_left > 0:
        m_left -= 1
        k -= 1
    else: #잉여 인원 모두 소진 -> 팀 줄어듦
        num = k // 3
        left = k % 3
        result -= num
        if left != 0:
            result -= 1
        
        k -= num * 3
        k -= left
        

print(result)
