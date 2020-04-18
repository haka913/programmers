from collections import defaultdict
genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]


def solution(genres, plays):
    dic = defaultdict(lambda: 0)
    for g, p in zip(genres, plays):
        print(g,p)
        dic[g] += p

    print(dic)
    answer = []
    return answer


print(solution(genres, plays))

# todo 베스트앨범
