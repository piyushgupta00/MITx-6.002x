cows={'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
def brute_force_cow_transport(cows,limit=10):
   cows_dict=cows.copy()
    
   from ps1_partition import get_partitions
   cowslist=list(cows.keys())
 
   def cargo_weight(cows,cowsdict):
     weight=0
     for cow in cows:
       weight=weight+cowsdict[cow]
     return weight
   
   def isValidTrip(cargo,limit,cows_dict):
     if cargo_weight(cargo,cows_dict)<=limit:
       return True
    
   

   FullPart=[]

   for item in (get_partitions(cowslist)):
       FullPart.append(item)

   FullPartSorted=sorted(FullPart,key=lambda x: len(x))
   
   for overall_trip in FullPartSorted:
       validTripCount=0
       for trip in overall_trip:
           if isValidTrip(trip,limit,cows_dict):
               validTripCount+=1
       if validTripCount==len(overall_trip):
           return overall_trip

result=brute_force_cow_transport(cows,limit=10)
print('the shortes trip transport is: ',result)