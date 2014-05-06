def schoolMultiplication(number1,number2):
    intermediateResults=[]
    memorizedFigure = 0
    
    for i in str(number2):
        intermediateString = ""
        for j in str(number1):
            figure = int(i)*int(j)%10 + memorizedFigure
            memorizedFigure = int(i)*int(j)/10
            intermediateString+=str(figure)
        intermediateResults.append(intermediateString)

    intermediateResults.reverse()
    result = 0
    for i in range(len(intermediateResults)):
        result += int(intermediateResults[i])*10**i

    return result

'''
#easy test
print "12*12=" + str(schoolMultiplication(12,12))
import random
a = random.randint(2**2048,2**2049)
b = random.randint(2**2048,2**2049)
print "Random multiplication: " + str(schoolMultiplication(a,b))
'''

def KaratsubaMultiplication(number1,number2):

    if number2 > number1:
        temp = number2
        number2 = number1
        number1 = temp
    
    n = len(str(number1))
    if n>len(str(number2)):
        zeros = ''
        for i in range(n-len(str(number2))):
            zeros+='0'
        str2 = zeros + str(number2)
        str1 = str(number1)
    else:
        str1 = str(number1)
        str2 = str(number2)

    if  n == 1:
        return number1*number2

    a = int(str1[0:(n+n%2)//2])    
    b = int(str1[(n+n%2)//2:]) 
    c = int(str2[0:(n+n%2)//2])    
    d = int(str2[(n+n%2)//2:])
    
    x = KaratsubaMultiplication(a,c)
    y = KaratsubaMultiplication(b,d)
    z = KaratsubaMultiplication((a+b),(c+d)) - x - y

    return x*(10**(n-n%2)) + z*(10**(n//2)) + y

'''
#easy test
for i in range(1,999):
    for j in range(1,999):
        if i*j != KaratsubaMultiplication(i,j):
            print "Alert! Some problems with ", i, j
        elif i%100==0 and j%100==0:
            print i,j #just to see progress
'''
