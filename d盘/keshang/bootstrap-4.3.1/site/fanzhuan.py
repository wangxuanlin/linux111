l = [1,2,3,4,5,6]
# b = []
# a = len(l) -1
# print(a)
# # print(l[::-1])
# for i in range(len(l)):
#   l[i] = l[a-i]
#   b.append(l[i])
# print(b)
i = 0
j = len(l) -1
while i < j:
  l [i], l[j] = l[j],l[i]
  i += 1
  j -= 1

print(l)






