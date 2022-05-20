import heapq
import sys

input = sys.stdin.readline
INF = 999

#그래프 입력 받기 시작

print("노드 라인 입력 : node line")
node, line = map(int, input().split() )
#노드 간선 입력

print("시작 노드 입력 : start")
start = int(input())
#시작 노드 결정

dist = [INF] * (node+1)
#최단 거리 INF로 초기화

graph = [[] for i in range(node+1)]

print("A노드에서 B노드 거리 입력 : nodeA nodeB cost")
for _ in range(line):
    nodeA, nodeB, cost = map(int, input().split())
    graph[nodeA].append((nodeB, cost)) 
#A노드에서 B노드 가는 거리 입력받고 그래프에 저장

#그래프 입력받기 끝
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    #큐 생성 큐와 dist 시작점 입력

    while q:
        distance, now = heapq.heappop(q)
        #최단거리 제일 짧은 노드 꺼내기

        if dist[now] < distance: 
            continue
        #이미 처리된 노드이면 무시
        
        for i in graph[now]:
            c = distance + i[1]
        # 현재 처리 중인 노드와 인접한 노드 계산

            if c < dist[i[0]]:
                dist[i[0]] = c
                heapq.heappush(q, (c, i[0]))
            # 계산한 거리가 더 짧을 경우 정보 갱신


dijkstra(start)

print("노드 : 최단거리")
for i in range(1, node+1):
    if dist[i] == INF:
        print("INF")
    else: 
        print(chr(i+64), "   :  ", dist[i])


