class Solution:
    def isNumber(self, s: str) -> bool:
        # Define states for the finite state machine
        states = [
            {"digit": 1, "sign": 2, "dot": 3},
            {"digit": 1, "dot": 4, "exp": 5},
            {"digit": 1, "dot": 3},
            {"digit": 4},
            {"digit": 4, "exp": 5},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7},
        ]
        
        current_state = 0
        
        for char in s:
            if char.isdigit():
                input_type = "digit"
            elif char in ['+', '-']:
                input_type = "sign"
            elif char == '.':
                input_type = "dot"
            elif char in ['e', 'E']:
                input_type = "exp"
            else:
                return False  # Invalid character
            
            if input_type not in states[current_state]:
                return False  # Invalid input for the current state
            current_state = states[current_state][input_type]
        
        # The number is valid if the final state is one of the accepting states (1, 4, 7)
        return current_state in [1, 4, 7]

        