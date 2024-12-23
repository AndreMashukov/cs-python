from collections import defaultdict

def add_to_k(arr, target, k):
  elems = {} # SW hashmap
  last_pair_start = -1 # max start of any pair
  count = 0 # result

  for i in range(k):
    complement = target - arr[i]
    if complement in elems:
        # if it's already ...
        last_pair_start = max(last_pair_start, elems[complement])
    # keep track of the last found index for this element
    elems[arr[i]] = i

    if last_pair_start != -1:
        # pair exists
        count += 1
  print(elems)

  #  a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7]  
  # {2: 0, 4: 1, 7: 9, 5: 7, 3: 4, 8: 6, 1: 8}

  for i in range(k, len(arr)):
    idx_removed = (i-k)

    if elems[arr[idx_removed]] == idx_removed:
        # all traces of this element have been removed
        del elems[arr[idx_removed]]
    
    if idx_removed == last_pair_start:
        # we lost our last pair
        last_pair_start = -1

    complement = target - arr[i] 
    if complement in elems:
        # saving complement's index because we are moving forward
        # this pair's gonna last as long as this index does
        last_pair_start = max(last_pair_start, elems[complement])
    
    elems[arr[i]] = i

    if last_pair_start != -1:
        count += 1
  return count

def contain_pair(a,m,k):
    return add_to_k(a, m, k)