def findProduct(A):
    result = 1
    isNegative = False
    for x in A:
        result = result * x
        if x < 0:
            isNegative = True
    return result, isNegative


def func(N, K, M, A):
    for i in range(M):
        product, isNegative = findProduct(A)
        if not isNegative:
                smallestIndex = A.index(min(A))
                A[smallestIndex] -= K
        else:
                largest = A[0]
                largestNegativeIndex = 0
                for i in range(len(A)):
                    if A[i] < 0 and A[i]>largest:
                        largestNegativeIndex = i
                A[largestNegativeIndex] += K

    return findProduct(A)[0]


N = 5
M = 2
K = 3
A = [1,3,-6,-5,-4]
print(func(N, K, M, A))
