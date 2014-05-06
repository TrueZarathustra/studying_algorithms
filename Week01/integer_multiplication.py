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
