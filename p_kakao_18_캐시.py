def solution(cacheSize, cities):
    cities = [i.lower() for i in cities]
    cache = []
    cost = 0
    if cacheSize == 0:
        return len(cities * 5)

    for city in cities:
        if city in cache:
            cost += 1
            cache.remove(cache[cache.index(city)])
            cache.insert(0,city)
        else:
            cost += 5
            if len(cache) == cacheSize:
                cache.pop()
            cache.insert(0, city)
    return cost


# print(solution(cacheSize=3, cities=['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(cacheSize=2, cities=['Jeju', 'Pangyo', 'NewYork', 'newyork']))
