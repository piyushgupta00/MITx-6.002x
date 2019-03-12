import math
def greedySum(alist,sum):
	'''Returns the maximum possible multiplier list for a given list and a SUM
	alist= An input list, sum= the sum we have to obtain'''
	rem_sum=sum
	mult_list=[]
	index=0
	while index <= len(alist)-1:
		curr_elem=alist[index]
		max_quot=math.floor(rem_sum/curr_elem)
		rem_sum=rem_sum - curr_elem*max_quot
		mult_list.insert(index,max_quot)
		#print(mult_list)
		index+=1
	if rem_sum!=0:
		return 'no solution'
	return mult_list
	
	
def main():
	list=[18,7,3,2,1]
	s=107
	print('hey there')
	print(greedySum(list,s))

if __name__=="__main__":
	main()
