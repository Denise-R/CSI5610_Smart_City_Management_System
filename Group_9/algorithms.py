from typing import List
import collections


def leastInterval(self, tasks: List[str], n: int) -> int:

    ct = collections.Counter(tasks) # Use Counter to sort tasks
    
    if n < 0 or n > 100: # Check for n input
        return -1

    if n == 0: # Check for n == 0 case
        return len(tasks)

    mc = ct.most_common(1)[0] # Get (one of) the most frequent tasks
    count = (mc[1]-1) * (n + 1) # calculate theoretical amount of space needed

    for k, v in ct.most_common(): # Iterate over all and increase count by each that is same as max frequency
        if v == mc[1]:
            count += 1

    return max(count, len(tasks)) # we do this to check for cases with too much granularity, mostly small frequenzies