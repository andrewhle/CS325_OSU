
def helper(A, S, index, result, curr):

    if S == 0:
        result.append(curr.copy())
    if S < 0:
        return
    prev = -1
    for i in range(index, len(A)):
        if A[i] == prev:
            continue
        curr.append(A[i])
        helper(A, S - A[i], i + 1, result, curr )
        curr.pop()

        prev = A[i]

    print(result)
    return result

def amount (A, S):
    
    A.sort(reverse=False)

    result = []
    return helper(A, S, 0, result, [])
  


amount([11, 1, 3, 2, 6, 1, 5], 8)

