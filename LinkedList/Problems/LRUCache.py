#User function Template for python3

# design the class in the most optimal way

"""
8

82 


SET 97 30 GET 43 GET 13 SET 48 56 GET 67 GET 60 SET 74 43 
SET 72 39 SET 100 59 GET 85 SET 91 62 GET 72 SET 1 4 GET 1 GET 53 
GET 5 SET 59 60 SET 18 95 GET 37 GET 61 GET 15 SET 66 38 GET 22 GET 10 
SET 33 1 GET 5 SET 57 59 SET 69 11 SET 29 70 SET 75 47 GET 6 GET 2 
SET 68 90 GET 27 GET 39 SET 1 6 GET 58 GET 49 SET 8 18 SET 70 98 GET 29 
SET 71 19 SET 81 93 GET 55 SET 44 8 GET 51 SET 89 86 GET 91 GET 35 
SET 84 26 SET 43 95 GET 92 SET 21 21 GET 39 GET 93 GET 23 GET 86 GET 95 
GET 9 GET 3 SET 23 85 SET 58 26 SET 93 3 GET 97 GET 31 GET 50 SET 57 13 
SET 49 55 GET 29 GET 58 GET 77 SET 21 98 SET 6 95 GET 83 GET 24 SET 16 37 
SET 54 85 SET 55 25 GET 37 GET 93 GET 59 GET 24

2

7 

Queries = SET 1 2 SET 2 3 SET 1 5 SET 4 5 SET 6 7 GET 4 GET 1

"""

from collections import OrderedDict 
  
class LRUCache2:
    """
    This is Geeks For Geeks Implementation
    
    """
    # initialising capacity 
    def __init__(self, capacity: int): 
        self.cache = OrderedDict() 
        self.capacity = capacity 
  
    # we return the value of the key 
    # that is queried in O(1) and return -1 if we 
    # don't find the key in out dict / cache. 
    # And also move the key to the end 
    # to show that it was recently used. 
    def get(self, key: int) -> int: 
        if key not in self.cache: 
            return -1
        else: 
            self.cache.move_to_end(key) 
            return self.cache[key] 
  
    # first, we add / update the key by conventional methods. 
    # And also move the key to the end to show that it was recently used. 
    # But here we will also check whether the length of our 
    # ordered dictionary has exceeded our capacity, 
    # If so we remove the first key (least recently used) 
    def set(self, key: int, value: int) -> None: 
        self.cache[key] = value 
        self.cache.move_to_end(key) 
        if len(self.cache) > self.capacity: 
            self.cache.popitem(last = False) 

class LRUCache:
    """
    This is my own implementation.
    """
        
    def __init__(self,cap):
        #cap: capacity of cache
        #code here
        self.size = cap
        self.cache = []
    
    #This method works in O(1)
    def get(self, key):
        #code here
        tracker = []
        for kv in self.cache:
            if key in kv:
                tracker.append(1)
                return kv[key]
        if not tracker:
            return -1
        
    #This method works in O(1)   
    def set(self, key, value):
        #code here
        if len(self.cache) > 0:
            tracker = []
            for ind,kv in enumerate(self.cache):
                if key in kv:
                    tracker.append(1)
                    if len(self.cache) >= self.size:
                        temp = self.cache.pop(ind)
                        self.cache.append({key:value})
                else:
                    tracker.append(0)
            if ((0 in tracker) and (1 not in tracker)):
                if len(self.cache) >= self.size:
                    temp = self.cache.pop(0)
                    self.cache.append({key:value})
                else:
                    self.cache.append({key:value})
        else:
            self.cache.append({key:value})

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry=int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        
        lru=LRUCache(cap)
        lru2 = LRUCache2(cap)
        
       
        i=0
        q=1
        while q<=qry:
            qtyp=a[i]
            
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                lru2.set(int(a[i+1]),int(a[i+2]))
                #print (lru.cache)
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                print(lru2.get(int(a[i+1])),end=' ')
                #print (lru.cache)
                i+=2
            q+=1
        print()
# } Driver Code Ends