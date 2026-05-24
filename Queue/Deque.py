from collections import deque

q = deque()

q.append("Pavan")
q.append("ram")
q.append("Ravan")
q.append("Sai")
print(q)

d = q.popleft()
print(f"Element poped: {d}")

print(len(q))