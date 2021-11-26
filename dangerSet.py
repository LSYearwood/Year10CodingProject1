def maxElements(dangerSet, N):
    dangerSet100 = []

    for j in range(len(dangerSet)):
        if len(dangerSet100) < N: 
            if dangerSet[j] not in dangerSet100:
                dangerSet100.append([dangerSet[j][0],dangerSet[j][1]])
        else:
            if dangerSet[j][0] > min(dangerSet100)[0]:
                row = dangerSet100.index(min(dangerSet100))
                dangerSet100[row][0] = dangerSet[j][0]
                dangerSet100[row][1] = dangerSet[j][1]
       
    print(dangerSet100)

list = [[3,50], [2,100],[1,20],[7,6],[5,20]]
maxElements(list,3)