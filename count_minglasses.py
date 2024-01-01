"""
This program calculates the minimum number of glasses needed to obtain an exact sum of K liters.

"""

def solution(N, K):
    # Initialize a table to store minimum combinations for each sum
    dp = [float('inf')] * (K + 1)

    dp[0] = 0

    # Calculate minimum combinations for each sum up to K
    for i in range(1, N + 1):
        for j in range(K, 0, -1):
            if j >= i:
                dp[j] = min(dp[j], dp[j - i] + 1)

    # If dp[K] is still infinity, there is no combination that adds up to K
    if dp[K] == float('inf'):
        return -1

    # Return the minimum number of glasses needed to obtain the exact sum K
    return dp[K]

# Example usage:
N = 5 # Number of glasses
K = 10 # Required liters of water
result = solution(N, K)
print("Minimum number of glasses to obtain exact K litres:", result)