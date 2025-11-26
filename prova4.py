#a = [1, "a", "capça", [2], 1, "a"] 
a = [10, 9, 8, 7, 6, 5, 1, 2, 3, 4]
# passar els elements de la llista a string
for i in range(len(a)):
    a[i] = str(a[i])
    # crear una nova llista string separat per guió
    print(a)


c = "capça" in a
print(c)
print (len(a))
c = a.pop(2)
a.clear()



a.sort
print(a)
for i in range(len)(a):
    print(a[i])