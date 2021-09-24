from collections import deque

deq = deque('geek')

print(deq)

deq.append('y')

deq.appendleft('k')
print(deq)

print(deq.pop())
print(deq.popleft())
print(deq)
;