from sys import stdin

N = int(stdin.readline())
q = []
for i in range(N) :
    A = stdin.readline().split()

    if A[0] == 'push' : q.append(A[1])      # push

    elif A[0] == 'pop' :                    # pop
        if q : print(q.pop(0))
        else : print(-1)

    elif A[0] == 'size' : print(len(q))     # size

    elif A[0] == 'empty' :                  # empty
        if len(q) == 0 : print(1)
        else : print(0)
            
    elif A[0] == 'front' :                  # front
        if len(q) == 0 : print(-1)
        else : print(q[0])

    elif A[0] == 'back' :                   # back
        if len(q) == 0 : print(-1)
        else : print(q[-1])