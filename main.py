# from src.container import Stack
# 
# s = Stack([1, 2, 3, 4, 5])
# s.foreach(lambda i: print((i**2)*(3*i) + 1))
# s.foreach(lambda i: s.foreach(lambda j: s.push(j)))
# 
# last = 0
# 
# for i in s:
#   i = i * 2
#   if i > last:
#     last = i
#   for j in s:
#     j = round((4 * j) / 3)
#     if j > last:
#       last = j
#     for k in s:
#       k = i + j
#       if k > last:
#         last = k
#       print(i*j*k*last)

from src.container import Stack

s = Stack()
print(s.peek())