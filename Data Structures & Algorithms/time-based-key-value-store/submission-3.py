
# Timestamps will always be in increasing order (sorted)
# The data structure that is needed will be the following:
# {key: list[(value,timestamp)]}
# The hashmap will let us add  by key in O(1) and the list of value ts pairs,
# will allow getting a value by in O(log n) by using binary search. Binary search can be applied 
# in this case because values will always be in increasing order ()

class TimeMap:

    def __init__(self):
        self._cache:dict[str,list[tuple[str,int]]] = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._cache:
            self._cache[key] = [(value,timestamp)]
            return
        self._cache[key].append((value,timestamp)) 
        
        

    def get(self, key: str, timestamp: int) -> str:
        # problem statement requires that if the provided `timestamp` does not
        # exist,and set was previously called on that key, we return the value
        # if the the most recent timestamp for that key is less than `timestamp`
        # If the key is not in the hashmap, "" is returned

        if key not in self._cache:
            return ""
        start,end = 0, len(self._cache[key])-1
        result = ""

        while start <= end:
            middle = start +  (end - start) // 2

            if self._cache[key][middle][1] <= timestamp:
                # stores potential result which is <= than `timestamp` this will ensure the
                # result is always the smallest timestamp that is closes to `timestamp`, for example,
                # if `timestamp = 15` and the smallest timestamps are `5` and `10`, `10` will be chosen,
                # as 10 will be the "most recent" timestamp for `15`
                result = self._cache[key][middle][0]
                start = middle+1
            else:
                end = middle -1

        return result
        





        
        
