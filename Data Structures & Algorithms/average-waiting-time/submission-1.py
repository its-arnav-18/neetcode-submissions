from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0
        chef_free_time = 0
        
        for arrival, time_needed in customers:
            # Chef starts when the customer arrives or when the chef finishes the previous order
            start_time = max(arrival, chef_free_time)
            finish_time = start_time + time_needed
            
            # Waiting time is from arrival to when the food is done
            total_waiting_time += (finish_time - arrival)
            
            # Update when the chef will be free next
            chef_free_time = finish_time
            
        return total_waiting_time / len(customers)
