def mergeSort(array):

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

'''
#pre-defined arrays for simple test
a = []
b = [3]
c = [7,1]
d = [4,3,11,64,75,31,12,44,88,12]
e = [34,23423,65,54,56,5,5,5,5,"44",45,"dsfsdf",0,-43333,3.4,True,None]
'''
