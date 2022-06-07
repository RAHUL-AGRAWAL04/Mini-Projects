import time
import random
import matplotlib.pyplot as plt 


INF = float('inf')

# Divide & Conquer(DNC) recursive approach to find minimum and maximum number in a list
def minMaxUsingDNC(A, left, right, minDNC=INF, maxDNC=-INF):
	# if list contains only one element
	if left == right:         
		if minDNC > A[right]:      
				minDNC = A[right]
		if maxDNC < A[left]:       
		    maxDNC = A[left]
		return minDNC, maxDNC

	# if list contains only two elements
	if right - left == 1:   
		if A[left] < A[right]:
			if minDNC > A[left]:   
				minDNC = A[left]
			if maxDNC < A[right]:  
				maxDNC = A[right]
		else:
			if minDNC > A[right]:  
				minDNC = A[right]
			if maxDNC < A[left]:   
				maxDNC = A[left]
		return minDNC, maxDNC

  # find mid element
	mid = (left + right) // 2

  # recur for left sublist
	minDNC, maxDNC = minMaxUsingDNC(A, left, mid, minDNC, maxDNC)

  # recur for right sublist
	minDNC, maxDNC = minMaxUsingDNC(A, mid + 1, right, minDNC, maxDNC)

	return minDNC, maxDNC


#naive method approach to find minimum and maximum number in a list

def minMaxUsingNaive(A):
	minNaive = INF
	maxNaive = -INF
	for i in A:
		if i < minNaive:
			minNaive = i
		if i > maxNaive :
			maxNaive = i
			
	return minNaive,maxNaive
		
		
		
#code for array creation with random numbers for input
listofinputs = []			#list to store input values
sizeofinput = []			#list to store input sizes
n=0										#temp var to define input size
for i in range(10):
	temp = []
	n+=10000								#incrementing array size by 30
	sizeofinput.append(n)
	
	#creating input array of size n
	for j in range(n):
		temp.append(random.randint(0,9999999))
		
	#appending in listofinputs
	listofinputs.append(temp)
	

executionTimeDNC= []		#list of execution time for Divide and conquer approach
executionTimeNaive = []		#list of execution time for Naive approach

#calculating time of execution for DNC and Naive methods
for A in listofinputs:
	startDNC = time.time()
	minDNC, maxDNC = minMaxUsingDNC(A, 0, len(A) - 1, INF, -INF)
	endDNC = time.time()
	executionTimeDNC.append(endDNC-startDNC)		#creating list of execution time for DNC approach
	print('DNC(Execution_time : {}) : Min = {}, Max = {} from list{}'.format(endDNC-startDNC, minDNC,maxDNC,len(A)//30))
	
	startNaive = time.time()
	minNaive, maxNaive = minMaxUsingNaive(A)
	endNaive = time.time()
	executionTimeNaive.append(endNaive - startNaive)		#creating list of execution time for Naive method
	
	print('Naive(Execution_time : {}) : Min = {}, Max = {} from list{}'.format(endNaive-startNaive,minNaive,maxNaive,len(A)//30))
	print()
	

	

#Building Graph using matplotlib

xNaive = executionTimeNaive			#list of execution time obtained by naive method
xDNC = executionTimeDNC					#list of execution time obtained by DNC method
y = sizeofinput								
 
#print(xNaive)
plt.plot(xDNC, y, label = 'Divide and Conquer Graph')
plt.plot(xNaive,y, label = 'Naive Graph')  
plt.xlabel('EXECUTION TIME')  
plt.ylabel('INPUT SIZE')  
plt.legend()
plt.title('EXPERIMNT-01') 
plt.show() 







