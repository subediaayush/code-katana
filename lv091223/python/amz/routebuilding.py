def getServedBuilding(buildingCount, routerLocation, routerRange):
    
    routerReach = [0] * len(buildingCount)

    for routerIndex in range(len(routerLocation)):
        currentRange = routerRange[routerIndex]
        routerPosition = routerLocation[routerIndex]

        routerStartReach = routerPosition - currentRange
        routerEndReach = routerPosition + currentRange
        start = max(1, routerStartReach)
        end = min(len(buildingCount), routerEndReach)

        for i in range(start - 1, end):
            routerReach[i] += 1
    
    reachedBuildings = 0
    for buildingIndex in range(len(buildingCount)):
        if (buildingCount[buildingIndex] <= routerReach[buildingIndex]):
            reachedBuildings += 1

    return reachedBuildings

print(getServedBuilding([1,2,1,2,2],[3,1],[1,2]))
print(getServedBuilding([2,1,1,3],[1,2],[2,0]))

