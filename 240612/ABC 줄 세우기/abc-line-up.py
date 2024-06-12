def solution():
    n = int(input())
    arr = input().split()
    string = "".join(arr)
    if is_answer(n, string):
        print(0)
    else:
        count = bubble_sort(arr)
        print(count)
    
def is_answer(n, string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_answer = alphabet[:n]
    
    if string == alphabet_answer:
        return True
    return False


def bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        # 이미 정렬된 경우를 위한 플래그
        swapped = False
        for j in range(0, n-i-1):
            # 인접한 두 요소를 비교하여 교환
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                count += 1
        # 만약 교환이 일어나지 않았다면 배열이 정렬된 상태이므로 종료
        if not swapped:
            break
    return count

solution()