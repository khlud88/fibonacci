def fibonacci_iterative(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
n_terms = 10
print(fibonacci_iterative(n_terms))
