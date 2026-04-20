import numpy

COEFF = numpy.array(input().split(), float)
X = float(input())
print(numpy.polyval(COEFF, X))
