list = [1,2,3,4,5,6,2,4,1,4,2,3,5,2]

def RemoveDublicate(list):
    Seen = set()
    unique = []
    for item in list:
        if item not in Seen:
            unique.append(item)
            Seen.add(item)
    return unique

print(RemoveDublicate(list))