from itertools import permutations 
  
  
# Get all permutations of [1, 2, 3] 
perm = permutations([0, 1, 2, 3]) 
  
# Print the obtained permutations 
for i in list(perm): 
    print (list(i)) 