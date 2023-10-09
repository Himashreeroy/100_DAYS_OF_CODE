class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        line_length = 0
        
        for word in words:
            # Check if adding the current word exceeds maxWidth
            if line_length + len(word) + len(line) > maxWidth:
                # Calculate total spaces needed for justification
                total_spaces = maxWidth - line_length
                # If there is only one word in the line, left-justify it
                if len(line) == 1:
                    result.append(line[0] + ' ' * total_spaces)
                else:
                    # Calculate spaces to be added between words
                    spaces_between_words = total_spaces // (len(line) - 1)
                    # Calculate extra spaces to be added from left
                    extra_spaces = total_spaces % (len(line) - 1)
                    # Construct the justified line
                    justified_line = ''
                    for i in range(len(line) - 1):
                        justified_line += line[i] + ' ' * (spaces_between_words + (1 if i < extra_spaces else 0))
                    justified_line += line[-1]
                    result.append(justified_line)
                
                # Reset line and line_length
                line = []
                line_length = 0
            
            # Add word to the current line
            line.append(word)
            line_length += len(word)
        
        # Left-justify the last line
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result
