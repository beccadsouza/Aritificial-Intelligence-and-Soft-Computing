import random
import sys

sys.setrecursionlimit(10000)

convergence_limit = 0


def genetic(p1, p2, p11, p22):
    global convergence_limit
    convergence_limit += 1
    for i in range(0, 2):
        p1[i] = p22[i]
        p2[i] = p11[i]

    print("Parents after crossover", p1, p2)
    for i in range(0, 2):
        if p1[i] == 0: p1[i] = 1
        else: p1[i] = 0
        if p2[i] == 0: p2[i] = 1
        else: p2[i] = 0

    print("Parents after mutations:", p1, p2)
    a = p1[0]
    b = p1[1]
    c = p1[2]

    ans1 = check(a, b, c)
    print("The output for p1 is", ans1)

    a = p2[0]
    b = p2[1]
    c = p2[2]
    ans2 = check(a, b, c)
    print("The output for p2 is", ans2)

    if ans1 == 1 or ans2 == 1:
        if ans1 == 1:
            print("One possible solution :", p1)
        elif ans2 == 1:
            print("One possible solution :", p2)
        return
    elif convergence_limit > 50:
        print("Convergen has been reached. No solution found")
        return
    else:
        p11 = p1[:]
        p22 = p2[:]
        genetic(p1, p2, p11, p22)


def check(a, b, c):
    d = a and b
    print("d is ", d)
    e = b or c
    print("e is ", e)
    q = not (d or e)
    return q


p1 = []
p2 = []

for i in range(0, 3):
    p1.append(random.randint(0, 1))
    p2.append(random.randint(0, 1))

if p1 == p2:
    p2 = []
    for i in range(0, 3):
        p2.append(random.randint(0, 1))

p11 = p1[:]
p22 = p2[:]

print("P1 is ", p1)
print("P2 is ", p2)
a = p1[0]
b = p1[1]
c = p1[2]

ans1 = check(a, b, c)
print("The output for p1 is", ans1)

a = p2[0]
b = p2[1]
c = p2[2]
ans2 = check(a, b, c)
print("The output for p2 is", ans2)

if ans1 == 1 or ans2 == 1:
    if ans1 == 1:
        print("One possible solution :", p1)
    elif ans2 == 1:
        print("One possible solutionn :", p2)
else:
    genetic(p1, p2, p11, p22)
