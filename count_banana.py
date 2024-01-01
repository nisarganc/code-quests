"""
This program counts the maximum number of times the word "BANANA" can be extracted from a string.
"""

def count_moves(s):
    # Count occurrences of 'B', 'A', and 'N' letters
    b_count = s.count('B')
    a_count = s.count('A')
    n_count = s.count('N')

    # Calculate the maximum number of moves for each letter
    moves_b = b_count
    moves_a = a_count // 3
    moves_n = n_count // 2

    # Return the feasible number of moves for the word "BANANA"
    return min(moves_b, moves_a, moves_n)

# Example usage:
s = "BASDFJNANGJKSADBIA"
result = count_moves(s)
print("Maximum number of moves:", result)