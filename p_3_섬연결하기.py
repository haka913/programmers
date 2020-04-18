parent = {}
rank = {}


def make_set(v):
    parent[v] = v
    rank[v] = 0


def findRoot(v):
    if parent[v] != v:
        parent[v] = findRoot(parent[v])
    return parent[v]


def union(root1, root2):
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def solution(n, costs):
    for i in range(n):
        make_set(i)

    kruskal_weight = 0
    costs = sorted(costs, key=lambda i: i[2])
    print(costs)
    for i in costs:
        v, u, w = i
        r1 = findRoot(v)
        r2 = findRoot(u)
        if r1 != r2:
            union(r1, r2)
            kruskal_weight += w

    return kruskal_weight


print(solution(n=4, costs=[[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))

# 크루스칼 알고리즘

# parent={}#각 노드의 부모
# rank={}#트리의 노드 수
#
# def make_set(v):#각 노드를 집합으로 만들기
#     parent[v]=v#일단 부모는 자기 자신
#     rank[v]=0#
# def findRoot(v):
#     if parent[v]!=v:#부모가 자기 자신이 아니면
#         parent[v]=findRoot(parent[v])#최상위의 부모로 갱신
#     return parent[v]#부모가 자기 자신이라면 최상위이므로 반환
# def union(r1,r2):
#     if r1!=r2:#루트값이 서로 다르면 다른 집합임
#         if rank[r1]>rank[r2]:#노드 수가 적은 집합의 루트가 노드 수가 많은 집합의 루트로 변경됨
#             parent[r2]=r1
#         else:
#             parent[r1]=r2
#             if rank[r1]==rank[r2]:#집합의 개수가 같다면
#                 rank[r2]+=1# r1이 속한 집합의 부모 루트가 r2로 변경되었으므로 r2의 개수를 더 많다고 해주기
# def solution(n,costs):
#     for i in range(n):#모든 노드에 대해 집합화
#         make_set(i)
#     #mst=[]#최소 비용 신장(spanning) 트리
#     s=0#최소 비용 누적을 위한 변수
#     costs=sorted(costs,key=lambda costs:costs[2])#비용 기준으로 정렬
#     for j in costs:
#         v,u,w=j# v=노드1 u=노드2 w=비용
#         r1=findRoot(v)#노드 v에 대한 루트
#         r2=findRoot(u)
#         if r1!=r2:#노드의 루트가 다르면
#             union(r1,r2)#두 노드 중 하나의 집합 수가 많은 집합에 넣기
#             s+=w
#             #mst.append(j)
#     return s #최단거리
#     #return mst #최단거리를 만들기 위해 선택된 노드,간선,비용들


# #other kruskal
# def solution(n, costs):
#     answer = 0
#
#     V = set()
#     for v1, v2, cost in costs:
#         V.add(v1)
#         V.add(v2)
#     sortedCosts = sorted(costs, key = lambda x: x[2])
#
#     visited = set()
#
#     visited.add(V.pop())
#     while V:
#         for i in range(len(sortedCosts)):
#             v1, v2, cost = sortedCosts[i]
#             if v1 in visited and v2 in visited:
#                 sortedCosts.pop(i)
#                 break
#             elif v1 in visited or v2 in visited:
#                 if v1 in V:
#                     V.remove(v1)
#                 if v2 in V:
#                     V.remove(v2)
#                 visited.add(v1)
#                 visited.add(v2)
#                 answer += cost
#                 sortedCosts.pop(i)
#                 break
#
#     return answer


# #to greedy
# def greedy_search(start,dic,n, cost_dic):
#     available = [i for i in range(n)]
#     available.remove(start)
#     queue = dic[start]
#     costs = [0 for i in range(n)]
#     answer = 0
#     k = 0
#     while available:
#         queue.sort(key = lambda x: (x[2],abs(k-x[0])))
#         print(queue)
#         start, finish, cost = queue.pop(0)
#         if finish in available:
#             available.remove(finish)
#             answer += cost_dic[(start,finish)]
#             nextNode = dic[finish]
#             queue = nextNode + queue
#             k = finish
#     return answer
#
# def solution(n, costs):
#     answer = 0
#     dic = {}
#     cost_dic ={}
#     for node in costs:
#         cost_dic[(node[0], node[1])] = node[2]
#         cost_dic[(node[1], node[0])] = node[2]
#         if dic.get(node[0])==None:
#             dic[node[0]] = [node]
#         else:
#             dic[node[0]].append(node)
#         if dic.get(node[1])==None:
#             dic[node[1]] = [[node[1],node[0],node[2]]]
#         else:
#             dic[node[1]].append([node[1],node[0],node[2]])
#
#
#
#     return greedy_search(0, dic,n,cost_dic)
