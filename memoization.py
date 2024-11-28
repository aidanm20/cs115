memo{}

def LCS(S1, S2):
    if (S1, S2) in memo:
        return memo[(S1, S2)]
    if S1 == "" or S2 == "":
        memo[(S1, S2)] = 0
        return 0
    elif S1[0] == S2[0]:
        answer = 1 + LCS(S1[1:], S2[1:])
        memo[(S1, S2)] = answer
        return answer
    else:
        chopS1 = LCS(S1[1:], S2)
        chopS2= LCS(S1, S2[1:])
        answer = max(chopS1, chopS2)
        memo[(S1, S2)] = answer
        return answer
