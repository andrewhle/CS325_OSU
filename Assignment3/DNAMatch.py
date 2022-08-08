
#["A","T","A","G","T","T","C","C","G","T","C","A","A","A"]
DNA1 = "ATAGTTCCGTCAAA"
DNA2 = "GTGTTCCCGTCAAA"

m = len(DNA1)
n = len(DNA2)

memo = [[0 for i in range(m+1)] for j in range (n+1)]

#

def dna_match_topdown (DNA1, DNA2, m, n, memo):
    if (m == 0 or n == 0):
        return 0
    elif memo[m-1][n-1] != 0:
        return memo[m][n]
    elif(DNA1[m-1] == DNA2[n-1]):
        memo[m-1][n-1] = 1 + dna_match_topdown(DNA1, DNA2, m-1, n-1, memo)
        return memo[m-1][n-1]
    else:
        memo[m-1][n-1] = max(dna_match_topdown(DNA1, DNA2, m, n-1, memo), dna_match_topdown(DNA1, DNA2, m-1, n, memo))
        return memo[m-1][n-1]


def dna_match_bottomup (DNA1, DNA2, m, n, memo):
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                memo[i][j] = 0
            elif DNA1[i-1] == DNA2[j-1]:
                memo[i][j] = 1 + memo[i-1][j-1]
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    return memo[m][n]


print(dna_match_topdown(DNA1, DNA2, m, n, memo))
print(dna_match_bottomup(DNA1, DNA2, m, n, memo))
