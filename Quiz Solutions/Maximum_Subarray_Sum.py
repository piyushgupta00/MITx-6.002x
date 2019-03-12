def max_subarray(A):
    '''finds the maximum subarray sum using Kadane's algorithm in
  O(n) time, also returns the start/end indices of the subarray''' 
    max_ending_here = max_so_far = A[0]
    start=end=0
    index=0
    for x in A[1:]:
      index+=1

      if max_ending_here+x < x:
        #start=A.index(x)
        start=index
      max_ending_here = max(x, max_ending_here + x)

      if max_ending_here > max_so_far:
        #end=A.index(x)
        end=index
      max_so_far = max(max_so_far, max_ending_here)
      
    return (max_so_far,start,end)
#sample test cases
alist=[-2, 3, 4, -3, 4]
alist2=[-2, -7, 6, 4, -6, 8, -4, -11]
print('Max Sub Array Sum is: ',max_subarray(alist2)[0])
print('starting and ending indices are {} - {}'\
.format(max_subarray(alist2)[1],max_subarray(alist2)[2]))
print()

