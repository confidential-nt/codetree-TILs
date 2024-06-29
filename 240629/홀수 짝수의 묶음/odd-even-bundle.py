def solution():
  n = int(input())
  arr = list(map(int, input().split()))
  even = []
  odd = []

  for i in range(n):
      if arr[i] % 2 == 0:
          even.append(arr[i])
      else:
          odd.append(arr[i])
  is_even_turn = True

  count = 0
  while True:
    if not len(odd) and not len(even):
      break
    if is_even_turn:
      if len(even):
        even.pop()
        count += 1  
      elif len(odd):
        if len(odd) < 2:
          break
        odd.pop()
        odd.pop()
        count += 1
      is_even_turn = False
      
    else:
      if len(odd):
        odd.pop()
        count += 1
      elif len(even) and len(odd):
        if not len(even):
          break
        if not len(odd):
          break
        even.pop()
        odd.pop()
        count += 1
      is_even_turn = True

  while len(even):
    even.pop()
    count -= 1
  while len(odd):
    odd.pop()
    count -= 1
  print(count)
solution()

# 최대한 수를 덜 써야함 -> 하나로 해결 가능하면 그거로 go
# 하나로 해결 못하면 사용해야하는 숫자를 늘려가면서 짝수(짝짝 홀홀), 혹은 홀수(짝홀)가 되는 조합을 찾아야 함. 숫자의 크기는 상관없음.
# 즉, 같은 성분(짝, 홀)이면 어떤 숫자든 노상관.
# 단, 모든 숫자를 다 사용해야함.... => 남으면 남은 숫자를 마지막 묶음에 추가한다.
# 홀/짝을 미리 분류해서 문제를 풀면 더 쉽게 풀 수 있지 않을까?

# 짝
# 홀 1 3 9 7 5 11 3
# n = 7


# 짝 2 
# 홀 11 17 13 1 15 3
# n = 7
# 2/ 11/ 17 13/ 1 / 15 3/

# 2 11 17 13 1 15 3