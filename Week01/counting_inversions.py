def mergeSort(array): #this function is needed by countInversionsRecursevely()

    def merge(a1,a2):
        n = len(a1)+len(a2)
        i=0
        j=0
        result = []
        for k in range(n):
            if a1[i]<a2[j]:
                result.append(a1[i])
                i+=1
            else:
                result.append(a2[j])
                j+=1
            if i>=len(a1):
                for l in range(j,len(a2)):
                    result.append(a2[l])
                break
            elif j>=len(a2):
                for l in range(i,len(a1)):
                    result.append(a1[l])
                break
        return result
            

    if len(array)<2:
        return array

    if len(array)==2:
        return [min(array),max(array)]

    return merge(mergeSort(array[0:len(array)/2]),mergeSort(array[len(array)/2:]))

def bruteForce(array):
    count = 0
    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[i] > array[j]:
                count +=1
    return count

def countInversionsRecursevely(array):

    def countMergeInversions(a1,a2):

        result = 0
        i,j=0,0
        for k in range(len(a1)+len(a2)+1):
            if a1[i]>a2[j]:
                result+=1
                j+=1
            else:
                i+=1
                result+=j
            if i>=len(a1):
                result-=j
                break
            elif j>=len(a2):
                result += (len(a1)-i-1)*len(a2)
                break
        return result

    if len(array) < 100:
        return bruteForce(array)
    
    x = countInversionsRecursevely(array[0:len(array)//2])
    y = countInversionsRecursevely(array[len(array)//2:])
    srtX = mergeSort(array[0:len(array)//2])
    srtY = mergeSort(array[len(array)//2:])
    z = countMergeInversions(srtX,srtY)

    return x+y+z
    

'''
#pre-defined arrays for easy test
a = []
b = [1]
c = [1,3,2]
d = [1,5,65,3,9,4,2,5]

import time
import random
array = []
for i in range(100000):
    array.append(random.randint(0,99))

#start_time = time.time()
#a = bruteForce(array)
#print time.time() - start_time, "seconds"

start_time = time.time()
b = countInversionsRecursevely(array)
print time.time() - start_time, "seconds"

'''
