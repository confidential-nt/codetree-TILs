def solution():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    answer = -1
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if not is_carry(nums[i],nums[j],nums[k]):
                    answer = max(answer, nums[i] + nums[j] + nums[k])
    print(answer)

def is_carry(a,b,c):
    l_a = [int(el) for el in str(a)][::-1]
    l_b = [int(el) for el in str(b)][::-1]
    l_c = [int(el) for el in str(c)][::-1]
    
    max_len = max(len(l_a), len(l_b), len(l_c))

    for i in range(max_len):
        a_el = l_a[i] if len(l_a) >= i + 1 else 0
        b_el = l_b[i] if len(l_b) >= i + 1 else 0
        c_el = l_c[i] if len(l_c) >= i + 1 else 0
        
        sums = a_el + b_el + c_el
        if sums >= 10:
            return True
    return False


solution()