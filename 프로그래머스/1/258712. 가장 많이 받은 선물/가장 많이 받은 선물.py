def solution(friends, gifts):
    n = len(friends)
    idx = {name: i for i, name in enumerate(friends)}

    giveCount = [[0]*n for _ in range(n)]

    for record in gifts:
        giver, receiver = record.split()
        giveCount[idx[giver]][idx[receiver]] += 1

    giveSum = [0]*n
    receiveSum = [0]*n
    for i in range(n):
        for j in range(n):
            giveSum[i] += giveCount[i][j]
            receiveSum[j] += giveCount[i][j]

    giftIndex = [giveSum[i] - receiveSum[i] for i in range(n)]

    nextGift = [0]*n

    for i in range(n):
        for j in range(i+1, n):
            gi_to_gj = giveCount[i][j]
            gj_to_gi = giveCount[j][i]

            if gi_to_gj > gj_to_gi:
                nextGift[i] += 1
            elif gj_to_gi > gi_to_gj:
                nextGift[j] += 1
            else:
                if giftIndex[i] > giftIndex[j]:
                    nextGift[i] += 1
                elif giftIndex[j] > giftIndex[i]:
                    nextGift[j] += 1
                    
    return max(nextGift)
