#Matrix is said to be a singular matrix if its determinant is equal to zero.


def check(M, x, y):
    return [row[: y] + row[y+1:] for row in (m[: x] + m[x+1:])]


def checkforsingular(M):
    n=len(m)
    if (n== 2):
        result = m[0][0]*m[1][1] - m[1][0]*m[0][1]
        return result

    d = 0
    for i in range(data):
        val= (-1)**i
        dt = checkforsingular(check(m, 0, i))
        d+= (val*m[0][i]*dt)
    return d