class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        total_cost = 0
        start_index = 0
        current_gas = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]
            
            # If current gas is negative, we can't start from the current station
            if current_gas < 0:
                start_index = i + 1  # Move to the next station
                current_gas = 0  # Reset current gas
            
        # If the total gas is greater than or equal to the total cost, a solution exists
        if total_gas >= total_cost:
            return start_index
        else:
            return -1
