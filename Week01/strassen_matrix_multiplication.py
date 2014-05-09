def strassenMM(m1,m2):

    n = len(m1)
    
    def initMatrix(num):
        m = []
        for i in range(num):
            m.append([])
            for j in range(num):
                m[i].append(0)
        return m
    
    def sumM(m1,m2):
        n=len(m1)
        result = initMatrix(n)
        for i in range(n):
            for j in range(n):
                result[i][j]=m1[i][j]+m2[i][j]
        return result

    def subM(m1,m2):
        n=len(m1)
        result = initMatrix(n)
        for i in range(n):
            for j in range(n):
                result[i][j]=m1[i][j]-m2[i][j]
        return result

    def MM2x2(m1,m2):
        result = initMatrix(2)
        result[0][0]=m1[0][0]*m2[0][0]+m1[0][1]*m2[1][0]
        result[0][1]=m1[0][0]*m2[0][1]+m1[0][1]*m2[1][1]
        result[1][0]=m1[1][0]*m2[0][0]+m1[1][1]*m2[1][0]
        result[1][1]=m1[1][0]*m2[0][1]+m1[1][1]*m2[1][1]
        return result

    if n==2:
        return MM2x2(m1,m2)

    A,B,C,D,E,F,G,H =[],[],[],[],[],[],[],[]
    for i in range(n/2):
        A.append(m1[0:n/2][i][0:n/2])
        B.append(m1[0:n/2][i][n/2:])
        C.append(m1[n/2:][i][0:n/2])
        D.append(m1[n/2:][i][n/2:])
        E.append(m2[0:n/2][i][0:n/2])
        F.append(m2[0:n/2][i][n/2:])
        G.append(m2[n/2:][i][0:n/2])
        H.append(m2[n/2:][i][n/2:])

    P1 = strassenMM(A,subM(F,H))
    P2 = strassenMM(sumM(A,B),H)
    P3 = strassenMM(sumM(C,D),E)
    P4 = strassenMM(D,subM(G,E))
    P5 = strassenMM(sumM(A,D),sumM(E,H))
    P6 = strassenMM(subM(B,D),sumM(G,H))
    P7 = strassenMM(subM(A,C),sumM(E,F))

    R00 = sumM(subM(sumM(P5,P4),P2),P6)
    R01 = sumM(P1,P2)
    R10 = sumM(P3,P4)
    R11 = subM(sumM(P1,P5),sumM(P3,P7))

    R = initMatrix(n)
    for i in range(n/2):
        for j in range(n/2):
            R[i][j]=R00[i][j]
            R[i][j+n/2]=R01[i][j]
            R[i+n/2][j]=R10[i][j]
            R[i+n/2][j+n/2]=R11[i][j]

    return R

import random
a = [[1,2],[3,4]]
b = [[1,2],[3,4]]
c = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
d = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

m16 = []
for i in range(16):
    m16.append([])
    for j in range(16):
        m16[i].append(random.randint(1,1000))

m64 = []
for i in range(64):
    m64.append([])
    for j in range(64):
        m64[i].append(random.randint(1,1000))

m256 = []
for i in range(256):
    m256.append([])
    for j in range(256):
        m256[i].append(random.randint(1,1000))

import time
start_time = time.time()
r16 = strassenMM(m16,m16)
print time.time() - start_time, "seconds (16x16)"

start_time = time.time()
r64 = strassenMM(m64,m64)
print time.time() - start_time, "seconds (64x64)"

start_time = time.time()
r256 = strassenMM(m256,m256)
print time.time() - start_time, "seconds (256x256)"
