import sys
import numpy

def main():
	filename=sys.argv[1]
	data=numpy.loadtxt(filename,delimiter=",")
	for row_mean in numpy.mean(data,axis=1):
		print(row_mean)

if __name__== "__main__":
	main()
