def solution():
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]

    answer = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if is_triangle(coords[i],coords[j],coords[k]):
                    answer = max(answer, get_area(coords[i],coords[j],coords[k]))
    print(answer)


def is_triangle(c1,c2,c3):
    x1,y1 = c1
    x2,y2 = c2
    x3,y3 = c3

    # (x3 - x2) * (y2 - y1)

    if y1 - y2 == 0 and x2 - x3 == 0:
        return True

    if x1 - x3 == 0 and y3 - y2 == 0:
        return True  

    return False

def get_area(c1,c2,c3):
    x1,y1 = c1
    x2,y2 = c2
    x3,y3 = c3

    return abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))





solution()