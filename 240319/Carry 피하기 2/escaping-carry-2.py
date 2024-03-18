def solution():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    answer = -1
    for i in range(n):
        for j in range(i+1,n): # 이런 디테일 매우 중요!
            for k in range(j+1,n):
                if not is_carry(nums[i],nums[j],nums[k]):
                    answer = max(answer, nums[i] + nums[j] + nums[k])
    print(answer)

def is_carry(a,b,c):
    # 숫자의 범위는 1 <= x <= 10,000 : 10000끼리 더해봤자 carry 없으므로,
    # 결국 천의 자리 숫자까지만 carry 발생하는지 비교하면 됨.

    if a % 10 + b % 10 + c % 10 >= 10:
        return True
    
    if a % 100 // 10 + b % 100 // 10 + c % 100 // 10 >= 10:
        return True
    
    if a % 1000 // 100 + b % 1000 // 100 + c % 1000 // 100 >= 10:
        return True

    if a % 10000 // 1000 + b % 10000 // 1000 + c % 10000 // 1000 >= 10:
        return True

    return False

solution()