
# A is the starting data
A = [4,6,8,4,7,1,3,9,1,5]
# B is the list of zeros wiith the legth of A
B = [0] * len(A)
#The total number of elements
N = len(A)

for i in range(N):
    #current element
    sum = A[i]
    #Checking if left neighbor exists
    if i > 0:
        sum += A[i-1]
    #Checking if right neighbor exists 
    if i < N-1:
        sum += A[i +1]
    #Calculatating the average 
    B[i] = sum // 3

#Printing
print(A)
print(B)



