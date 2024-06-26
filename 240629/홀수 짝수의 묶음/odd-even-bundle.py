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
    if is_even_turn:
      if len(even):
        even.pop()
        count += 1  
      elif len(odd) >= 2:
        odd.pop()
        odd.pop()
        count += 1
      else:
        # 이 경우 홀수가 남아있을 경우 무조건 홀수는 2개 미만으로 남아있음.
        # 홀수를 쓸 경우 2개씩 쓰기 때문에 is_even_turn이 False일때와는 달리
        # 이런 처리를 해줘야하는 것.
        # 이 경우 짝수도 사실 남아있지 않음. (따라서 len(even) > 0 조건문 없어도 정답처리.)
        # 남은 홀수는 그룹에 포함시켜야함.
        if len(even) > 0 or len(odd) > 0:
          count -= 1
        break
      is_even_turn = False
    else:
      # 홀수 + 짝수는 의미없음 => 숫자를 최대한 덜 사용해야하는 상황에서 홀 + 짝 = 이미 홀임. 근데 짝수 더하기 전에도 홀임. 낭비.
      if len(odd):
        odd.pop()
        count += 1
      else:
        # 짝 -> 다음에 홀임. 홀이 없다는 것은 더 이상 그룹을 지을 수 없다는 것을 의미. break.
        break
      is_even_turn = True

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

# 거의 맞긴 했는데 틀린이유
# 1. # 홀수 + 짝수는 의미없음 => 숫자를 최대한 덜 사용해야하는 상황에서 홀 + 짝 = 이미 홀임. 근데 짝수 더하기 전에도 홀임. 낭비.
# 2.  # 짝 -> 다음에 홀임. 홀이 없다는 것은 더 이상 그룹을 지을 수 없다는 것을 의미. break.
# 3. # 이 경우 홀수가 남아있을 경우 무조건 홀수는 2개 미만으로 남아있음.
        # 홀수를 쓸 경우 2개씩 쓰기 때문에 is_even_turn이 False일때와는 달리
        # 이런 처리를 해줘야하는 것.
        # 이 경우 짝수도 사실 남아있지 않음. (따라서 len(even) > 0 조건문 없어도 정답처리.)
        # 남은 홀수는 그룹에 포함시켜야함.


# 그리고 나도 파악했다 시피 숫자는 중요한 게 아니므로 홀-짝의 수만 가지고도 문제를 풀 수 있음.