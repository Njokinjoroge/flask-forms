from itertools import product

def find_expressions(N, M):
    num_str = "".join(str(i) for i in range(1, N + 1))  # Construct the number sequence
    length = len(num_str) - 1  # Positions where we can insert '+'
    
    results = []
    
    # Generate all possible ways to insert '+' or keep numbers together
    for pattern in product(["", "+"], repeat=length):
        expression = "".join(num_str[i] + pattern[i] for i in range(length)) + num_str[-1]
        if eval(expression) == M:
            results.append(expression + "=" + str(M))
    
    return results

# Example usage:
N, M = map(int, input("Enter N and M: ").split())
solutions = find_expressions(N, M)

if solutions:
    print("Solutions:", " | ".join(solutions))
else:
    print("No solutions found.")
