cows={'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
import time
start= time.time()
def greedy_cow_transport(cows,limit=10):
    cowslist=list(cows.items())
    revcowslist=sorted(cowslist,key=lambda x:x[1],reverse=True)
    
    
    overalltrip=[]
    
    while len(revcowslist)>0:
      total_weight=0
      currenttrip=[]
      revcowslist_copy=revcowslist.copy()
      b=len(revcowslist_copy)
      
      for i in range(b):
        if  (total_weight+revcowslist_copy[i][1])<=limit:
          currenttrip.append(revcowslist_copy[i][0])
          
          total_weight=total_weight+revcowslist_copy[i][1]
          revcowslist.remove(revcowslist_copy[i])
      
      #print(currenttrip)
      overalltrip.append(currenttrip)
      
      
    #print()
    #print(overalltrip)
    return overalltrip

trip=greedy_cow_transport(cows)
print(trip)
end=time.time()
print(-start+end)
