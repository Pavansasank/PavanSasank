list = [1,2,3,4,5,6,2,4,1,4,2,3,5,2]

def frequencyCount(list):
    freq ={}
    for item in list:
        if item in freq:
            freq[item]+=1
        else:
            freq[item] = 1
    return freq
print(frequencyCount(list))