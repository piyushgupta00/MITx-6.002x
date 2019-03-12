import random

def update_step(current,update):
  nextstep=[]
  for i in range(2):
    nextstep.append(current[i]+update[i])
  return nextstep

def distance(point1,point2):
  xdist_sq=abs(point1[0]-point2[0])**2
  ydist_sq=abs(point1[1]-point2[1])**2

  return (xdist_sq+ydist_sq)**0.5
  
    

def random_walks(walks):
  position=[0,0]
  left_update=[-1,0]
  right_update=[1,0]
  top_update=[0,1]
  down_update=[0,-1]
  move=['left','right','top','down']
  #print('Starting from: ',position)
  random.seed(0)
  
  for i in range(walks):

     nextmove=random.choice(move)
     #print('move taken: ',nextmove)
     if nextmove=='left':
       position=update_step(position,left_update)
     if nextmove=='right':
       position=update_step(position,right_update)
     if nextmove=='top':
       position=update_step(position,top_update)
     if nextmove=='down':
       position=update_step(position,down_update)
     
     
     #print('Current Position: ',position)
     #print()
  
  return position
N=int(input('Enter the number of random walks to be taken: '))
#walks=random_walks(N)
origin=[0,0]
total=0
for i in range(100):
 final_dist=round(distance(random_walks(N),origin),2)
 total+=final_dist

#print('final distance from origin is: ',final_dist)
print('Expected distance from origin is: ',round(total/100,3))
