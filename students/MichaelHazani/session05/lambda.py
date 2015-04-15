Correct:
return[lambda x,e=i: x+c for i in range(n)]

Naive:
[(lambda x: x + e) for e in range(n)]
The wrong thing about it is that it will only return the largest e!
