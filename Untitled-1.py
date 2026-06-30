def goldbach(n):
     for i in range(2, n):
        if is_prime(i):
            for j in range(2, n):
                for k in range(2, n):
                    if j % 2 == 0:
                        if i + 2*k**2 == j:
                             return [i, j, k]
                for k in range(2, n):
                    if j % 2 == 1
                    if i + 2*k**2 = j
                    return [i,j,k]
