def solution(S, P, Q):
    
    seqCount = [] * len(S)
    itrCount = { 'A': 0, 'C':0, 'G':0, 'T': 0}
    for i in range(len(S)):
        seqCount.append({'A': itrCount['A'], 'C': itrCount['C'], 'G': itrCount['G'], 'T': itrCount['T']})
        itrCount[S[i]] = itrCount[S[i]] + 1

    print(seqCount)

    seqRes = []
    for i in range(len(P)):
        l = P[i]
        r = Q[i]

        res = 4
        if (seqCount[r]['A'] - seqCount[l]['A'] > 0):
            res = 1
        elif (seqCount[r]['C'] - seqCount[l]['C'] > 0):
            res = 2
        elif (seqCount[r]['G'] - seqCount[l]['G'] > 0):
            res = 3
        seqRes.append(res)

    return seqRes

print(solution('CAGCCTA', [2,5,0], [4,5,6]))
    