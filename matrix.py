import numpy # importing package

N,M = map(int, input().split()) # spliting inputs into variables

numpy.set_printoptions(sign=' ')
print(numpy.eye(N,M,k=1))       # printing matrix
