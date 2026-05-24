def Clean(names):
    left = 0 
    for right in range(len(names)):
        if names[left] != names[right]:
            left+=1
            names[left] = names[right]
    return left+1

names = ['a','a','b','c','c','d']
a =Clean(names)
print(names[:a])